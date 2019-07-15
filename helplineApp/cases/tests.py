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

from .models import Case
from incidences.models import Incidence
from perpetrators.models import Perpetrator
from victims.models import Victim
from reports.models import Report
from users.models import User

# Create your tests here.

from .models import Report

class CaseModelTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        
        self.report = Report.objects.create(
                        info = 'testing',
                        report_date = '2019-11-02T00:00:00+05:00',
                        case_opened = 'no'
                    )

        self.victim = Victim.objects.create(
            first_name = 'first_name',
            last_name = 'last_name',
            middle_name = 'middle_name',
            location = 'location',
            date_of_birth = '2019-11-02'
        )

        self.perpetrator = Perpetrator.objects.create(
            first_name = 'first_name',
            last_name = 'last_name',
            middle_name = 'middle_name',
            location = 'location',
            national_id_number = 'national_id_number'
        )

        self.user = User.objects.create_user(
            "test_username",
            "test_email@email.com",
            1,
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

        self.case = Case.objects.create(
                        incidence = self.incidence,
                        date = 'date',
                        location = 'location',
                        reported_to = 'reported_to',
                        case_no = 'case_no',
                        lawyer = 'lawyer',
                        police_station = 'police_station',
                        court = 'court',
                        user = self.user
                    )

        self.unauthorised_user = User.objects.create_user(
            "test_unauthorised_username",
            "test_unauthorised_email@email.com",
            1,
        )

        self.user.user_type = 1
        self.client = APIClient()
        self.anonymous_client = APIClient()
        self.unauthorised_client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.unauthorised_client.force_authenticate(user=self.unauthorised_user)


    def create_case(self, incidence, date, location, reported_to, case_no, lawyer, police_station, court, user):
        return Case.objects.create(
                            incidence = incidence,
                            date = date,
                            location = location,
                            reported_to = reported_to,
                            case_no = case_no,
                            lawyer = lawyer,
                            police_station = police_station,
                            court = court,
                            user = user
                            )


    def test_create_case(self):
        c = self.create_case(
                            self.incidence,
                            '2019-11-02',
                            'location',
                            'reported_to',
                            'case_no',
                            'lawyer',
                            'police_station',
                            'court',
                            self.user
                        )
        self.assertTrue(isinstance(c, Case))
        # self.assertEqual(c.__str__(), c.incidence.victim.first_name)


    def test_api_can_view_a_case(self):
        response = self.client.get('/api/cases/')
        self.assertEqual(response.status_code, 200) 


    def test_api_can_create_an_case(self):
        response = self.client.post('/api/cases/create/',
                                    json.dumps({
                                    'incidence': self.incidence.id,
                                    'date':'2019-11-02',
                                    'location':'location',
                                    'reported_to':'reported_to',
                                    'case_no':'case_no',
                                    'lawyer':'lawyer',
                                    'police_station':'police_station',
                                    'court':'court',
                                    'user':self.user.id
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 201)


    def test_api_can_update_a_case(self):
        response = self.client.put('/api/cases/'+str(self.case.id)+'/update/',
                                    json.dumps({
                                    'incidence': self.incidence.id,
                                    'date':'2019-11-02',
                                    'location':'location',
                                    'reported_to':'reported_to',
                                    'case_no':'case_no',
                                    'lawyer':'lawyer',
                                    'police_station':'police_station',
                                    'court':'court',
                                    'user':self.user.id,
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200) 


    def test_api_can_view_a_case_unauthorised_user(self):
        response = self.anonymous_client.get('/api/cases/')
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_a_case_unauthorised_user(self):
        response = self.anonymous_client.put('/api/cases/'+str(self.case.id)+'/update/',
                                    json.dumps({
                                    'incidence': self.incidence.id,
                                    'date':'2019-11-02',
                                    'location':'location',
                                    'reported_to':'reported_to',
                                    'case_no':'case_no',
                                    'lawyer':'lawyer',
                                    'police_station':'police_station',
                                    'court':'court',
                                    'user':self.user.id,
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


    def test_api_can_update_a_case_anonymous_user(self):
        response = self.anonymous_client.put('/api/cases/'+str(self.case.id)+'/update/',
                                    json.dumps({
                                    'incidence': self.incidence.id,
                                    'date':'2019-11-02',
                                    'location':'location',
                                    'reported_to':'reported_to',
                                    'case_no':'case_no',
                                    'lawyer':'lawyer',
                                    'police_station':'police_station',
                                    'court':'court',
                                    'user':self.user.id
                                    }),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 401) 


