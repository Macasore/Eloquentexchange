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