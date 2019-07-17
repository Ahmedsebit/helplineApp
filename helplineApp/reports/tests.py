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
from .models import Report
from users.models import User

# Create your tests here.

from .models import Report

class ReportModelTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        
        self.report = Report.objects.create(
                        info = 'testing',
                        report_date = '2019-11-02T00:00:00+05:00',
                        case_opened = 'no',
                        message_from = '70000000'
                    )
        self.user = User.objects.create_user(
            "test_username",
            "test_email@email.com",
            1,
        )

        self.client = APIClient()
        self.client2 = APIClient()
        self.client.force_authenticate(user=self.user)


    def create_report(self, info, report_date, case_opened, message_from):
        return Report.objects.create(
                                info = info,
                                report_date = report_date,
                                case_opened = case_opened,
                                message_from = message_from
                                )


    def test_report_creation(self):
        r = self.create_report(
                            'testing',
                            '2019-11-02T00:00:00+05:00',
                            'no',
                            '70000000'
                        )
        self.assertTrue(isinstance(r, Report))
        self.assertTrue(r.info =="testing")
        self.assertEqual(r.__str__(), r.info)


    
    def test_creation_report_opened_report(self):
        with self.assertRaises(ValidationError):
            self.create_report(
                            'testing',
                            '2019-11-02T00:00:00+05:00',
                            'yes',
                            '70000000'
                        ).full_clean()

    
    def test_creation_report_invalid_date(self):
        with self.assertRaises(ValidationError):
            self.create_report(
                            'testing',
                            '2010-11-02T00:00:00+05:00',
                            'no',
                            '70000000'
                        ).full_clean()


    def test_get_report_all_api(self):
        request = self.client.get('/api/reports/')
        self.assertEqual(request.status_code, 200)

    
    def test_create_report_api(self):
        request = self.client.post('/api/reports/create/',
                                    json.dumps({
                                        'info':'testing',
                                        'report_date':'2019-11-02T00:00:00+05:00',
                                        'case_opened':'no',
                                        'message_from':'70000000'
                                        }),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 201)


    def test_get_report_detail_api(self):
        request = self.client.get('/api/reports/'+str(self.report.id)+'/')
        self.assertEqual(request.status_code, 200)


    def test_get_report_all_api_invalid_user(self):
        request = self.client2.get('/api/reports/')
        self.assertEqual(request.status_code, 401)

    
    def test_get_report_detail_api_invalid_user(self):
        request = self.client2.get('/api/reports/'+str(self.report.id)+'/')
        self.assertEqual(request.status_code, 401)


    # def test_get_flight_delete_api(self):
    #     request = self.client.delete('/api/reports/'+str(self.flight.id)+'/delete/')
    #     self.assertEqual(request.status_code, 204)

    

