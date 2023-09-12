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
from django.views import View
from django.http import JsonResponse
import os
from urllib.parse import urlparse, parse_qs

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
    
def csrf_token_view(request):
    return render(request, 'csrf_token_page.html')

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