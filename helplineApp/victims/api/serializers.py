from rest_framework import serializers

from victims.models import Victim

class VictimModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Victim
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'location',
            'date_of_birth'
        ]

class VictimModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Victim
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'location',
            'date_of_birth'
        ]