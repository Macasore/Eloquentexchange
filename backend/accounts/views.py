from django.http import HttpResponse
from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from .serializers import EmailSerializer
from django.conf import settings
from rest_framework.permissions import AllowAny
from requests_oauthlib import OAuth1
from urllib.parse import urlencode
from rest_framework.views import APIView
from django.http.response import  HttpResponseRedirect
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import AuthTokenError
from social_core.backends.oauth import BaseOAuth1


def activate_user(request, uid, token):
    # Handle your GET request logic here
    # Extracted `uid` and `token` are available as function parameters

    # Construct the POST request data
    post_data = {
        'uid': uid,
        'token': token,
    }

    # Define the URL for the POST request
    post_url = 'http://localhost:8000/auth/users/activation/'

    # Make the POST request
    response = requests.post(post_url, data=post_data)

    # Handle the response as needed
    if response.status_code == 204:
        # POST request was successful

        # Render the 'activation.html' template
        return render(request, 'activation/activation.html', {})

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
            redirect_url = "http://localhost:3000"
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
# class RedirectSocial(View):
#     def get(self, request, *args, **kwargs):
#         code, state = str(request.GET['code']), str(request.GET['state'])
#         data = {'code': code,
#                 'state': state,
#                 'grant_type': 'authorization_code',
#             'client_id': os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),  
#             'client_secret': os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
#                 }
#         token_url = 'http://localhost:8000/auth/o/google-oauth2/'

#         response = requests.post(token_url, data=data)

#         # Check if the POST request was successful
#         if response.status_code == 200:
#             token_data = response.json()
#             access_token = token_data.get('access_token')
#             refresh_token = token_data.get('refresh_token')

#             return JsonResponse({'access_token': access_token, 'refresh_token': refresh_token})
#         else:
#             print('Failed to exchange code for tokens.')
#             return JsonResponse({'error': 'Failed to exchange code for tokens'}, status=400)
#         print(json_obj)
#         return JsonResponse(json_obj)
 
# @permission_classes([AllowAny])
# def redirect_social(request):
#     # Get the code and state from the URL query parameters
#     query_params = request.GET
#     code = query_params.get('code')
#     state = query_params.get('state')

#     if code and state:
#         # Construct the POST request data
#         token_url = 'http://localhost:8000/auth/o/google-oauth2/'
#         data = {
#             'code': code,
#             'state': state,
#             'grant_type': 'authorization_code',
#             'client_id': os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),  # Replace with your Google OAuth2 client ID
#             'client_secret': os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'),  # Replace with your Google OAuth2 client secret
#             'redirect_uri': 'http://localhost:8000/accounts/profile/',  # Replace with your redirect URI
#         }

#         # Make the POST request to exchange the code for tokens
#         response = requests.post(token_url, data=data)

#         # Check if the POST request was successful
#         if response.status_code == 200:
#             token_data = response.json()
#             access_token = token_data.get('access_token')
#             refresh_token = token_data.get('refresh_token')

#             # Return the access and refresh tokens in the response
#             return JsonResponse({'access_token': access_token, 'refresh_token': refresh_token})
#         else:
#             error_message = 'Failed to exchange code for tokens.'
#             return JsonResponse({'error': error_message}, status=400)
#     else:
#         error_message = 'Code and/or state not found in the callback URL.'
#         return JsonResponse({'error': error_message}, status=400)