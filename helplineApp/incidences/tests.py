import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory
from  django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import force_authenticate
import json

from .models import Incidence
from victims.models import Victim
from perpetrators.models import Perpetrator
from users.models import User

# Create your tests here.

from .models import Report

class ReportModelTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.report = Report.objects.create(
                        info = 'testing',
                        report_date = '2019-11-02T00:00:00+05:00',
                        case_opened = 'no'
                    )
        self.user = User.objects.create_user(
            "test_username",
            "test_email@email.com",
            1,
        )
        self.user.user_type = 1
        self.unauthorised_user = User.objects.create_user(
            "test_unauthorised_username",
            "test_unauthorised_email@email.com",
            1,
        )
        self.victim = Victim.objects.create(
            first_name = 'first_name',
            last_name = 'last_name',
            middle_name = 'middle_name',
            location = 'location',
            date_of_birth = '2010-11-02'
        )
        self.perpetrator = Perpetrator.objects.create(
            first_name = 'first_name',
            last_name = 'last_name',
            middle_name = 'middle_name',
            location = 'location',
            national_id_number = '20191102'
        )
        self.incidence = Incidence.objects.create(
                        victim = self.victim,
                        perpetrator = self.perpetrator,
                        peritraumatic_fear = 'no',
                        injury = 'no',
                        rape_type = 'FR',
                        memory_of_rape = 'no',
                        perpetrator_intimate_partner = 'no',
                        perpetrator_a_stranger = 'no',
                        prior_rape_history = 'no',
                        history_of_previous_rape = 'no',
                        investigator = self.user
        )
        self.report = Report.objects.create(
                        info = 'testing',
                        report_date = '2019-11-02T00:00:00+05:00',
                        case_opened = 'no'
                    )

        self.client = APIClient()
        self.anonymous_client = APIClient()
        self.unauthorised_client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.unauthorised_client.force_authenticate(user=self.unauthorised_user)

    def create_incidence(self, reported_case, victim, perpetrator, peritraumatic_fear, injury, rape_type, memory_of_rape, perpetrator_intimate_partner, perpetrator_a_stranger, prior_rape_history, history_of_previous_rape, investigator):
        return Incidence.objects.create(
                                reported_case = reported_case,
                                victim = self.victim,
                                perpetrator = self.perpetrator,
                                peritraumatic_fear = 'no',
                                injury = 'no',
                                rape_type = 'FR',
                                memory_of_rape = 'no',
                                perpetrator_intimate_partner = 'no',
                                perpetrator_a_stranger = 'no',
                                prior_rape_history = 'no',
                                history_of_previous_rape = 'no',
                                investigator = self.user
                                )


    def test_create_incidence(self):
        i = self.create_incidence(
                            self.report,
                            'no',
                            'no',
                            'FR',
                            'no',
                            'no',
                            'no',
                            'no',
                            'no',
                            self.victim,
                            self.perpetrator,
                            self.user
                        )
        self.assertTrue(isinstance(i, Incidence))
        self.assertTrue(i.victim.first_name =="first_name")
        self.assertTrue(i.__str__(), i.victim.first_name)


    def test_api_can_view_an_incidence(self):
        response = self.client.get('/api/incidences/')
        self.assertEqual(response.status_code, 200) 


    def test_api_can_create_an_incidence(self):
        response = self.client.post('/api/incidences/create/',
                                    json.dumps({
                                    'reported_case':self.report.id,
                                    'peritraumatic_fear':'no',
                                    'injury':'no',
                                    'rape_type':'FR',
                                    'memory_of_rape':'no',
                                    'perpetrator_intimate_partner':'no',
                                    'perpetrator_a_stranger':'no',
                                    'prior_rape_history':'no',
                                    'history_of_previous_rape':'no',
                                    'victim':self.victim.id,
                                    'perpetrator':self.perpetrator.id,
                                    'investigator':self.user.id,
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 201) 


    def test_api_can_update_an_incidence(self):
        response = self.client.put('/api/incidences/'+str(self.incidence.id)+'/update/',
                                    json.dumps({
                                    'reported_case':self.report.id,
                                    'peritraumatic_fear':'no',
                                    'injury':'no',
                                    'rape_type':'FR',
                                    'memory_of_rape':'no',
                                    'perpetrator_intimate_partner':'no',
                                    'perpetrator_a_stranger':'no',
                                    'prior_rape_history':'no',
                                    'history_of_previous_rape':'no',
                                    'victim':self.victim.id,
                                    'perpetrator':self.perpetrator.id,
                                    'investigator':self.user.id,
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200) 


    def test_api_can_update_an_incidenceanonymous_user(self):
        response = self.client.put('/api/incidences/'+str(self.perpetrator.id)+'/update/',
                                    json.dumps({
                                    'reported_case':self.report.id,
                                    'peritraumatic_fear':'no',
                                    'injury':'no',
                                    'rape_type':'FR',
                                    'memory_of_rape':'no',
                                    'perpetrator_intimate_partner':'no',
                                    'perpetrator_a_stranger':'no',
                                    'prior_rape_history':'no',
                                    'history_of_previous_rape':'no',
                                    'victim':self.victim.id,
                                    'perpetrator':self.perpetrator.id,
                                    'investigator':self.user.id,
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200)


    def test_api_can_view_an_incidence_unauthorised_user(self):
        response = self.anonymous_client.get('/api/incidences/')
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_an_incidence_unauthorised_user(self):
        response = self.anonymous_client.put('/api/incidences/'+str(self.perpetrator.id)+'/update/',
                                    json.dumps({
                                    'reported_case':self.report.id,
                                    'peritraumatic_fear':'no',
                                    'injury':'no',
                                    'rape_type':'FR',
                                    'memory_of_rape':'no',
                                    'perpetrator_intimate_partner':'no',
                                    'perpetrator_a_stranger':'no',
                                    'prior_rape_history':'no',
                                    'history_of_previous_rape':'no',
                                    'victim':self.victim.id,
                                    'perpetrator':self.perpetrator.id,
                                    'investigator':self.user.id,
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_an_incidencet_anonymous_user(self):
        response = self.anonymous_client.put('/api/perpetrators/'+str(self.perpetrator.id)+'/update/',
                                    json.dumps({
                                    'reported_case':self.report.id,
                                    'peritraumatic_fear':'no',
                                    'injury':'no',
                                    'rape_type':'FR',
                                    'memory_of_rape':'no',
                                    'perpetrator_intimate_partner':'no',
                                    'perpetrator_a_stranger':'no',
                                    'prior_rape_history':'no',
                                    'history_of_previous_rape':'no',
                                    'victim':self.victim.id,
                                    'perpetrator':self.perpetrator.id,
                                    'investigator':self.user.id,
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 

