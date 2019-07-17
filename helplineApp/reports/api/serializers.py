from rest_framework import serializers

from reports.models import Report

class ReportModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Report
        fields = [
            'info',
            'report_date',
            'case_opened',
            'message_from'
        ]

class ReportModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = [
            'info',
            'report_date',
            'case_opened',
            '70000000'
        ]