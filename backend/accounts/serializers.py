from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        
class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    message = serializers.CharField()