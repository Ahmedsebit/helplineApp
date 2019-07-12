from rest_framework import serializers

from perpetrators.models import Perpetrator

class PerpetratorModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Perpetrator
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'location',
            'national_id_number'
        ]

class PerpetratorModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perpetrator
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'location',
            'national_id_number'
        ]