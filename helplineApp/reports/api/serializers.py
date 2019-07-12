from rest_framework import serializers

from reports.models import Report

class ReportModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Report
        fields = [
            'info',
            'report_date',
            'case_opened'
        ]

class ReportModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = [
            'info',
            'report_date',
            'case_opened'
        ]