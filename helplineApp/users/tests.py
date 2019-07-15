from django.test import TestCase
from django.urls import reverse_lazy
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory

import json
import sys
import tempfile
from django.test import override_settings
from .models import User

# Create your tests here.

class UserModelTest(TestCase):

    def setUp(self):
        self.authorised_user = User.objects.create_user(
            "test_username",
            "test_email@email.com",
            "test_password"
        )
        self.authorised_user.user_type = 1
        self.unauthorised_user = User.objects.create_user(
            "test_authorised_username",
            "test_authorised_email@email.com",
            "test_password"
        )

        self.authorised_user.user_type = 2

        self.client = APIClient()
        self.anonymous_client = APIClient()
        self.authorised_client = APIClient()
        self.client.force_authenticate(user=self.authorised_user)
        self.authorised_client.force_authenticate(user=self.authorised_user)


    def test_create_username(self):
        self.assertTrue(isinstance(self.authorised_user, User))


    def test_api_can_resister_a_user(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200) 


    def test_api_can_update_a_user(self):
        response = self.client.put('/api/users/'+str(self.authorised_user.id)+'/update/',
                                    json.dumps({
                                    "password": "test_password_2"}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200) 


    def test_api_can_update_a_user_not_user(self):
        response = self.client.put('/api/users/'+str(self.unauthorised_user.id)+'/update/',
                                    json.dumps({
                                    "password": "test_password_2"}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)


    def test_api_can_resister_a_user_unauthorised_user(self):
        response = self.anonymous_client.get('/api/users/')
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_a_user_unauthorised_user(self):
        response = self.anonymous_client.put('/api/users/'+str(self.authorised_user.id)+'/update/',
                                    json.dumps({
                                    "password": "test_password_2"}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_a_user_not_user_unauthorised_user(self):
        response = self.anonymous_client.put('/api/users/'+str(self.authorised_user.id)+'/update/',
                                    json.dumps({
                                    "password": "test_password_2"}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


    # def test_api_can_resister_a_user_not_manager(self):
    #     response = self.unauthorised_client.get('/api/users/')
    #     self.assertEqual(response.status_code, 401) 