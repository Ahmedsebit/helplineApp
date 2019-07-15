from django.test import TestCase
from django.urls import reverse_lazy
from django.test import TestCase
from django.core.exceptions import ValidationError

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory

import json
import sys
import tempfile
from django.test import override_settings

from .models import Victim
from users.models import User

# Create your tests here.

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            "test_username",
            "test_email@email.com",
            "test_password"
        )
        self.user.user_type = 2
        self.unauthorised_user = User.objects.create_user(
            "test_unauthorised_username",
            "test_unauthorised_email@email.com",
            "test_password"
        )
        self.unauthorised_user.user_type = 1
        self.victim = Victim.objects.create(
            first_name = 'first_name',
            last_name = 'last_name',
            middle_name = 'middle_name',
            location = 'location',
            date_of_birth = '2019-11-02'
        )
        self.client = APIClient()
        self.anonymous_client = APIClient()
        self.unauthorised_client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.unauthorised_client.force_authenticate(user=self.unauthorised_user)


    def create_victim(self, first_name, last_name, middle_name, location, date_of_birth):
        return Victim.objects.create(
                                first_name = 'first_name',
                                last_name = 'last_name',
                                middle_name = 'middle_name',
                                location = 'location',
                                date_of_birth = '2019-11-02'
                                )


    def test_create_victim(self):
        self.assertTrue(isinstance(self.victim, Victim))


    def test_creation_victim_invalid_date(self):
        with self.assertRaises(ValidationError):
            self.create_victim(
                            'first_name',
                            'last_name',
                            'middle_name',
                            'location',
                            '2010-11-02'
                        ).full_clean()

    
    def test_api_can_view_a_victim(self):
        response = self.client.get('/api/victims/')
        self.assertEqual(response.status_code, 200) 


    def test_api_can_create_a_victim(self):
        response = self.client.post('/api/victims/create/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'date_of_birth':'2019-11-02'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 201) 


    def test_api_can_update_a_victim(self):
        response = self.client.put('/api/victims/'+str(self.victim.id)+'/update/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'date_of_birth':'2019-11-02'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200) 


    def test_api_can_update_a_victim_anonymous_user(self):
        response = self.client.put('/api/victims/'+str(self.victim.id)+'/update/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'date_of_birth':'2019-11-02'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)


    def test_api_can_view_a_victim_unauthorised_user(self):
        response = self.anonymous_client.get('/api/victims/')
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_a_victim_unauthorised_user(self):
        response = self.anonymous_client.put('/api/victims/'+str(self.victim.id)+'/update/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'date_of_birth':'2019-11-02'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_a_user_not_user_unauthorised_user(self):
        response = self.anonymous_client.put('/api/victims/'+str(self.victim.id)+'/update/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'date_of_birth':'2019-11-02'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


    # def test_api_can_resister_a_user_not_manager(self):
    #     response = self.client3.get('/api/victims/')
    #     self.assertEqual(response.status_code, 401) 