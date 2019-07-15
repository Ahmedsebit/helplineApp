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

from .models import Perpetrator
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
        self.perpetrator = Perpetrator.objects.create(
            first_name = 'first_name',
            last_name = 'last_name',
            middle_name = 'middle_name',
            location = 'location',
            national_id_number = 'national_id_number'
        )
        self.client = APIClient()
        self.anonymous_client = APIClient()
        self.unauthorised_client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.unauthorised_client.force_authenticate(user=self.unauthorised_user)


    def test_create_victim(self):
        p = self.perpetrator = Perpetrator.objects.create(
            first_name = 'first_name',
            last_name = 'last_name',
            middle_name = 'middle_name',
            location = 'location',
            national_id_number = 'national_id_number'
        )
        self.assertTrue(isinstance(self.perpetrator, Perpetrator))
        self.assertEqual(p.__str__(), p.first_name)

    
    def test_api_can_view_a_perpetrators(self):
        response = self.client.get('/api/perpetrators/')
        self.assertEqual(response.status_code, 200) 


    def test_api_can_create_a_victim(self):
        response = self.client.post('/api/perpetrators/create/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'national_id_number':'national_id_number'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 201) 


    def test_api_can_update_a_perpetrators(self):
        response = self.client.put('/api/perpetrators/'+str(self.perpetrator.id)+'/update/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'national_id_number':'national_id_number'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200) 


    def test_api_can_update_a_perpetrator_anonymous_user(self):
        response = self.client.put('/api/perpetrators/'+str(self.perpetrator.id)+'/update/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'national_id_number':'national_id_number'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)


    def test_api_can_view_a_perpetrator_unauthorised_user(self):
        response = self.anonymous_client.get('/api/perpetrators/')
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_a_perpetrator_unauthorised_user(self):
        response = self.anonymous_client.put('/api/perpetrators/'+str(self.perpetrator.id)+'/update/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'national_id_number':'national_id_number'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_a_perpetrator_not_user_unauthorised_user(self):
        response = self.anonymous_client.put('/api/perpetrators/'+str(self.perpetrator.id)+'/update/',
                                    json.dumps({
                                    'first_name':'first_name',
                                    'last_name':'last_name',
                                    'middle_name':'middle_name',
                                    'location':'location',
                                    'national_id_number':'national_id_number'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


    # def test_api_can_resister_a_user_not_manager(self):
    #     response = self.client3.get('/api/perpetrators/')
    #     self.assertEqual(response.status_code, 401) 