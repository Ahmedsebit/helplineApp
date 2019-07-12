from django.contrib.auth import get_user_model
from django.utils.timesince import timesince
from rest_framework import serializers
from django.urls import reverse_lazy
from users.models import User

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'user_type',
            'password'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ('username', 'first_name', 'last_name', 'email','password')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ('password')