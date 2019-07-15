from rest_framework import serializers

from cases.models import Case

class CaseModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Case
        fields = [
            'incidence',
            'location',
            'reported_to',
            'case_no',
            'lawyer',
            'police_station',
            'court',
            'user'
        ]

class CaseModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = [
            'incidence',
            'location',
            'reported_to',
            'case_no',
            'lawyer',
            'police_station',
            'court',
            'user'
        ]