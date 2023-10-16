from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.core.mail import send_mail, EmailMessage
from rest_framework.decorators import api_view, permission_classes
from .serializers import EmailSerializer, PaymentSerializer, PackageSerializer, CoinSerializer, BuyCryptoSerializer, WalletSerializer, SellCryptoSerializer, CombinedCryptoSerializer, SellCryptoSerializerfilter
from django.conf import settings
from rest_framework.permissions import AllowAny
from requests_oauthlib import OAuth1
from urllib.parse import urlencode
from rest_framework.views import APIView
from django.http.response import  HttpResponseRedirect
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import AuthTokenError
from social_core.backends.oauth import BaseOAuth1
from rest_framework import status
from rest_framework.views import APIView
from .models import Payment, Package, Coin, BuyCrypto, Wallets, SellCrypto, ReferralCode, UserAccount
import uuid
from rest_framework import viewsets
import os, json
import urllib.parse
from djoser.views import UserViewSet
import string
import random
from django.dispatch import receiver
from djoser import signals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.shortcuts import redirect
from django.contrib import messages


def activate_user(request, uid, token):
    post_data = {
        'uid': uid,
        'token': token,
    }
    current_hostname = request.get_host()
    if settings.DEBUG == True:
        base_url = "http://" + current_hostname
    else:
         base_url = "https://" + current_hostname


    activation_endpoint = "/auth/users/activation/"

    post_url = base_url + activation_endpoint

    response = requests.post(post_url, data=post_data)

    if response.status_code == 204:
        
        messages.success(request, "Activation Successful")
        # return JsonResponse({
        #     "message": "Activation Successful",
        #     "link": "https://eloquentexchange.org/dashboard"
        # }, status=status.HTTP_200_OK)
        return redirect("https://eloquentexchange.org/sign-in")

    else:
        # POST request failed
        return HttpResponse('GET request successful, but POST request failed', status=500)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def send_email(request):
    serializer = EmailSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        name = serializer.validated_data['name']
        message = serializer.validated_data['message']
        subject = "Contact Form Submission"
        
        message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        try:
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return Response({'message': 'Email sent successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return requests.Response(serializer.errors, status=400)

@permission_classes([AllowAny])
class TwitterAuthRedirectEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        try:
            oauth = OAuth1(
                      settings.SOCIAL_AUTH_TWITTER_KEY, 
                      client_secret=settings.SOCIAL_AUTH_TWITTER_SECRET
            )
             #Step one: obtaining request token
            request_token_url = "https://api.twitter.com/oauth/request_token"
            data = urlencode({
                      "oauth_callback": settings.TWITTER_AUTH_CALLBACK_URL
            })
            response = requests.post(request_token_url, auth=oauth, data=data)
            response.raise_for_status()
            response_split = response.text.split("&")
            oauth_token = response_split[0].split("=")[1]
            oauth_token_secret = response_split[1].split("=")[1]  

                #Step two: redirecting user to Twitter
            twitter_redirect_url = (
         f"https://api.twitter.com/oauth/authenticate?oauth_token={oauth_token}"
            )
            return HttpResponseRedirect(twitter_redirect_url)
        except ConnectionError:
             html="<html><body>You have no internet connection</body></html>"
             return HttpResponse(html, status=403)
        except:
              html="<html><body>Something went wrong.Try again.</body></html>"
              return HttpResponse(html, status=403)
          
@permission_classes([AllowAny])
class TwitterCallbackEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        try:
            oauth_token = request.query_params.get("oauth_token")
            oauth_verifier = request.query_params.get("oauth_verifier")

            # Load the strategy and backend
            strategy = load_strategy(request)
            backend = load_backend(strategy, BaseOAuth1)
            
            # Exchange the OAuth token for access and refresh tokens
            user = backend.do_auth(
                access_token=oauth_token,
                response_type='token',
                redirect_uri=None,  # Twitter does not require this
                user=None
            )

            # You can now access user.tokens['oauth_token'] and user.tokens['oauth_token_secret']

            # Redirect to your desired URL
            redirect_url = "https://eloquentexchange.org"
            return HttpResponseRedirect(redirect_url)

        except AuthTokenError:
            return HttpResponse(
                "<html><body>Failed to exchange tokens. Please try again.</body></html>",
                status=403
            )
        except Exception as e:
            return HttpResponse(
                f"<html><body>Something went wrong: {e}</body></html>",
                status=403
            )

       
class PaymentInitiationView(APIView):
    def post(self, request):
        amount = request.data.get('amount')
        reference = str(uuid.uuid4())
        currency = request.data.get('currency')
        package = request.data.get('package')
        user = request.user

        payment = Payment.objects.create(amount=amount, status='pending', reference=reference, package=package, user=user)
        user = payment.user
        email = user.email
        
        flutterwave_response = self.initialize_payment(payment.reference, amount, email, currency)
        if flutterwave_response.get('status'):
            payment.status = 'initialized'
            payment.save()
            # authorization_url = paystack_response['data']['authorization_url']
            # return redirect(authorization_url)
            return Response(flutterwave_response, status=status.HTTP_201_CREATED)
        else:
            payment.status = 'failed'
            payment.save()
            print("Flutterwave Error:", flutterwave_response)
            return Response({'error': 'Payment initialization failed'}, status=status.HTTP_400_BAD_REQUEST)
        
    def initialize_payment(self, reference, amount, email, currency):
        flutterwave_url = 'https://api.flutterwave.com/v3/payments'
        secret_key = settings.FLUTTERWAVE_SECRET_KEY
        headers = {
            'Authorization': f'Bearer {secret_key}',
            'Content-Type': 'application/json',
        }
        # amount = amount * 100
        data = {
            'tx_ref': reference,
            'amount': amount,
            'currency': currency,
            'customer': {
                'email': email
            },
            'customizations': {
                'title': "EloquentExchange Payment"
            },
            'redirect_url': 'https://eloquentexchange.org/dashboard'
        }
        
        response = requests.post(flutterwave_url, headers=headers, json=data)
        return response.json()
    
@permission_classes([AllowAny]) 
class PackageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
@permission_classes([AllowAny])   
class CoinViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =Coin.objects.all()
    serializer_class = CoinSerializer
@permission_classes([AllowAny])   
class WalletViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Wallets.objects.all()
    serializer_class = WalletSerializer
        
# @csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def webhook(request):
    secret_hash = os.getenv("FLW_SECRET_HASH")
    signature = request.headers.get("verifi-hash")
    if signature == None or (signature != secret_hash):
        return HttpResponse(status=401)
    
    payload = request.body.decode('utf-8')
    response = HttpResponse(status=200)
    data = json.loads(payload)
    email = data["customer"]["email"]
    status = data["status"]
    reference = data["txRef"]

    if status == 'successful' or status == 'SUCCESSFUL':

        try:
            payment = Payment.objects.get(reference=reference)
            payment.status = status
            payment.save()
            selected_package = payment.package
            package_link = {
                'Beginners': os.getenv("Beginners"),
                'Intermediate': os.getenv("Intermediate"),
                'Pro': os.getenv("Pro")
            }
            link = package_link[selected_package]
            message_body = f"Thank you for purchasing the {selected_package} Package.\n Please click here to join your program: {link}\n\n Thanks for using our site.\n The EloquentExchange team"
            subject= "ELOQUENT EXCHANGE PACKAGE LINK"
            
            try:
                send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
                )
                return Response({'message': 'package purchase success'})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Payment.DoesNotExist:
            try:
                purchase = BuyCrypto.objects.get(reference=reference)
                coin = Coin.objects.get(name=purchase.coin_type)
                purchase.status = status
                purchase.save()
                message_body = f"Coin: {purchase.coin_type}\n Network: {purchase.network}\n Wallet-Address: {purchase.wallet_address}\n Amount-paid: {purchase.amount}$\n Rate: {coin.rate}$ per 1 {coin.name}\n Email: {email}\n"
                subject= "COIN PURCHASE"
                
                try:
                    send_mail(
                    subject,
                    message_body,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                    )
                    return Response({'message': 'coin purchase success'})
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except purchase.DoesNotExist:
                return ("Reference does not exist")
        
    else:
        payment = Payment.objects.get(reference=reference)
        payment.status = status
        payment.save()
    
    return (response)


class PurchaseCryptoView(APIView):
    def post(self, request):
        amount = request.data.get('amount')
        coin_type = request.data.get('coin_type')
        reference = str(uuid.uuid4())
        network = request.data.get('network')
        wallet_address = request.data.get('wallet_address')
        trans_type = 'Bought'
        user = request.user
        referrer = ReferralCode.objects.get(owner=user)
        reward = referrer.usage_count * 0.5
        amount = float(amount) - reward

        purchase = BuyCrypto.objects.create(amount=amount, status='pending', reference=reference, coin_type=coin_type,
                                            network=network, wallet_address=wallet_address,
                                            trans_type=trans_type, user=user)
        serializer = BuyCryptoSerializer(purchase)
        user = purchase.user
        email = user.email
        
        flutterwave_response = self.initialize_payment(purchase.reference, amount, email, currency="usd")
        if flutterwave_response.get('status'):
            purchase.status = 'initialized'
            purchase.save()
            # authorization_url = paystack_response['data']['authorization_url']
            # return redirect(authorization_url)
            return Response(flutterwave_response, status=status.HTTP_201_CREATED)
        else:
            purchase.status = 'failed'
            purchase.save()
            print("Flutterwave Error:", flutterwave_response)
            return Response({'error': 'Payment initialization failed'}, status=status.HTTP_400_BAD_REQUEST)
        
    def initialize_payment(self, reference, amount, email, currency):
        flutterwave_url = 'https://api.flutterwave.com/v3/payments'
        secret_key = settings.FLUTTERWAVE_SECRET_KEY
        headers = {
            'Authorization': f'Bearer {secret_key}',
            'Content-Type': 'application/json',
        }
        # amount = amount * 100
        data = {
            'tx_ref': reference,
            'amount': amount,
            'currency': currency,
            'customer': {
                'email': email
            },
            'customizations': {
                'title': "EloquentExchange Payment"
            },
            'redirect_url': 'https://eloquentexchange.org/dashboard'
        }
        
        response = requests.post(flutterwave_url, headers=headers, json=data)
        return response.json()


@api_view(['POST'])
def sellcrypto(request):
    if request.method == 'POST':
        try:
            serializer = SellCryptoSerializer(data=request.data)
            if serializer.is_valid():
                # serializer.save(user=request.user)
                amount = serializer.validated_data.get('amount')
                trans_type = 'Sold'
                coin_type = serializer.validated_data.get('coin_type')
                account_number = serializer.validated_data.get('account_number')
                bank = serializer.validated_data.get('bank')
                sender_address = serializer.validated_data.get('sender_address')
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
            
            wallet = SellCrypto.objects.create(amount=amount, trans_type=trans_type, coin_type=coin_type, account_number=account_number, bank=bank, user=request.user, sender_address=sender_address)
            user = wallet.user
            user_email = user.email
            
            # cleaned_filename = clean_filename(proof_of_payment.name)
            # fs = FileSystemStorage()
            # filename = fs.save(cleaned_filename, proof_of_payment)
            # attachment_path = proof_of_payment.url
            
            # with open(attachment_path, 'rb') as file:
            #     file_content = file.read()
                
            # mime_type = magic.from_buffer(file_content, mime=True)
            coin = Coin.objects.get(name=wallet.coin_type)
            subject= "SELLING OF COIN"
            message_body = f"Coin: {coin_type}\n Amount of Crypto sent in dollars: {amount}\n Rate: {coin.rate} per 1$  Account_no: {account_number}\n Bank: {bank}\n Email: {user_email}\n Sender's Address: {sender_address}"
                
            try:
                email = EmailMessage(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                )
                email.send()
                # file.close()
                
                return JsonResponse({'message': 'Proof of payment sent successfully'})
            except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    return JsonResponse({'error': 'Invalid request method'}, status=405)
            

class CryptoTransactionListView(generics.ListAPIView):
    serializer_class = CombinedCryptoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = self.request.user
        buy_queryset = BuyCrypto.objects.filter(user=user)
        sell_queryset = SellCrypto.objects.filter(user=user)
        
        combined_data = []
        
        if not buy_queryset.exists() and not sell_queryset.exists():
            return Response({'message': 'No transactions found for this user.'}, status=status.HTTP_200_OK)
        
        for buy_crypto_obj in buy_queryset:
            buy_serializer = BuyCryptoSerializer(buy_crypto_obj) if buy_crypto_obj else None
            if buy_serializer:
                combined_data.append(buy_serializer.data)

        for sell_crypto_obj in sell_queryset:
            sell_serializer = SellCryptoSerializerfilter(sell_crypto_obj) if sell_crypto_obj else None
            if sell_serializer:
                combined_data.append(sell_serializer.data)

        return Response(combined_data, status=status.HTTP_200_OK)
    
class BoughtCryptoTransactionListView(generics.ListAPIView):
    serializer_class = BuyCryptoSerializer  
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        buy_queryset =  BuyCrypto.objects.filter(user=user)
        
        combined_data = []
        
        for buy_crypto_obj in buy_queryset:
            buy_serializer = BuyCryptoSerializer(buy_crypto_obj) if buy_crypto_obj else None
            if buy_serializer:
                combined_data.append(buy_serializer.data)
                
        return Response(combined_data, status=status.HTTP_200_OK)
        
        
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

class SoldCryptoTransactionListView(generics.ListAPIView):
    serializer_class = SellCryptoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        sell_queryset = SellCrypto.objects.filter(user=user)
        
        combined_data = []
        
        for sell_crypto_obj in sell_queryset:
            sell_serializer = SellCryptoSerializerfilter(sell_crypto_obj) if sell_crypto_obj else None
            if sell_serializer:
                combined_data.append(sell_serializer.data)

        return Response(combined_data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def purchasealternative(request):
    purpose_of_payment = request.data.get('purpose_of_payment')
    item = request.data.get('item3')
    transaction_name = request.data.get('transaction_name')
    amount = request.data.get('amount')
    network = request.data.get('network')
    wallet_address = request.data.get('wallet_address')
    coin_type = request.data.get('coin_type')
    reference = str(uuid.uuid4())
    package = request.data.get('package')
    user = request.user
    
    if purpose_of_payment == 'purchase-coin':
        trans_type = 'Bought'
        purchase = BuyCrypto.objects.create(amount=amount, status='pending', reference=reference,
                                            coin_type=coin_type,
                                            network=network, wallet_address=wallet_address,
                                            trans_type=trans_type, user=user)
        user = purchase.user
        email = user.email
        coin = Coin.objects.get(name=purchase.coin_type)
        message_body = f"Coin: {purchase.coin_type}\n Network: {purchase.network}\n Wallet-Address: {purchase.wallet_address}\n Amount-paid: {purchase.amount}$\n Rate: {coin.rate}$ per 1 {coin.name}\n Email: {email}\n TRANSACTION NAME: {transaction_name}"
        subject= "COIN PURCHASE"
        try:
            email = EmailMessage(
            subject,
            message_body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            )
            email.send()
            # file.close()
            
            return JsonResponse({'message': 'coin purchase successful'})
        except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
    elif purpose_of_payment == 'purchase-package':
         payment = Payment.objects.create(amount=amount, status='pending',
                                          reference=reference, package=package,
                                          user=user)
         user = payment.user
         email = user.email
         message_body = f"Amount Paid: {amount}$\n Package: {package}\n Email: {email}\n TRANSACTION NAME: {transaction_name}"
         subject= "PACKAGE PURCHASE"
         
         try:
             send_mail(
             subject,
             message_body,
             settings.EMAIL_HOST_USER,
             [settings.EMAIL_HOST_USER],
             fail_silently=False,
             )
             return Response({'message': 'package purchase successful'})
         except Exception as e:
             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
    else:
        return Response("Invalid purpose")
    

class ApplyReferral(APIView):
    def post(self, request):
        referral_code = request.data.get('referral_code')
        user = request.user

        try:
            referral = ReferralCode.objects.get(code=referral_code)
        except ReferralCode.DoesNotExist:
            return Response({'error': 'Invalid referral code'}, status=status.HTTP_400_BAD_REQUEST)

        if referral.owner == user:
            return Response({'error': 'Self-referral is not allowed'}, status=status.HTTP_400_BAD_REQUEST)

        # Increase the usage count of the referral code
        referral.usage_count += 1
        referral.save()

        # Associate the user with the referrer
        user.referrer = referral.owner
        user.save()

        return Response({'message': 'Referral applied successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_referral_code(request):
    user = request.user
    referral_code = user.referral_code

    if referral_code:
        return Response(referral_code)
    else:
        return Response({'message': 'Referral code not available'}, status=404)

@api_view(['POST'])
@permission_classes([AllowAny])
def check_referral_code(request):
    referral_code = request.data.get("referral_code")
    try:
        ReferralCode.objects.get(code=referral_code)
        return HttpResponse(status=status.HTTP_200_OK)
    except ReferralCode.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def generate_referral_code(length=6):
            characters = string.ascii_letters + string.digits
            return ''.join(random.choice(characters) for _ in range(length))
@permission_classes([AllowAny])
class CustomUserViewSet(UserViewSet):
    @receiver(signals.user_registered)
    def custom_user_registered(sender, user, request, **kwargs):

        referral_code = request.data.get("referral_code")
        user = user
        
        if referral_code:
            try:
                try:
                    referrer = ReferralCode.objects.get(code=referral_code)
                except:
                    print("Referral code invalid")
                referrer.usage_count += 1
                referrer.save()
                user_2 = UserAccount.objects.get(email=request.data.get("email"))
                user_2.referral_code = generate_referral_code()
                user_2.save()
                ReferralCode.objects.create(code=user_2.referral_code, owner=user_2)
            except ReferralCode.DoesNotExist:
               raise ValueError("Referral code does not exist")
            
        else:

            email=request.data.get("email")

            user_1 = UserAccount.objects.get(email=email)

            user_1.referral_code = generate_referral_code()
            user_1.save()
            
            new_referral_code = user_1.referral_code
            referral_owner = user_1  # Change this to the appropriate user
            ReferralCode.objects.create(code=new_referral_code, owner=referral_owner)
            

        
        
    
