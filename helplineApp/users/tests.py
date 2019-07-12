from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse_lazy
from django.test import TestCase
from django.contrib.auth.models import User
from django.core import management
from django.core.management import call_command
from django.utils.six import StringIO
from rest_framework.test import APIClient
from rest_framework import status
import json
from rest_framework.authtoken.models import Token
import sys
import tempfile
from django.test import override_settings
from .models import CustomUser

# Create your tests here.

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            "test_username",
            "test_first_name",
            "test_last_name",
            "test_email@email.com",
            1,
            "test_password"
        )
        self.user2 = User.objects.create_user(
            "test_username_2",
            "test_first_name_2",
            "test_last_name_2",
            "test_email_2@email.com",
            1,
            "test_password_2"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def test_create_username(self):
        self.assertTrue(isinstance(self.user, CustomUser))


    def test_api_can_resister_a_user(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200) 


    def test_api_can_update_a_user(self):
        response = self.client.put('/api/users/'+str(self.user.id)+'/update/',
                                    json.dumps({
                                    "password": "test_password_2"}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200) 

    def test_api_can_update_a_user_not_user(self):
        response = self.client.put('/api/users/'+str(self.user2.id)+'/update/',
                                    json.dumps({
                                    "password": "test_password_2"}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200) 

