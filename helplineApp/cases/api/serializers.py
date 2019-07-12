from rest_framework import serializers

from cases.models import Case

class CaseModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Case
        fields = [
            'victim',
            'perpetrator',
            'reported_case',
            'location',
            'reported_to',
            'case_no',
            'lawyer',
            'police_station',
            'court'
        ]

class CaseModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = [
            'victim',
            'perpetrator',
            'reported_case',
            'location',
            'reported_to',
            'case_no',
            'lawyer',
            'police_station',
            'court'
        ]