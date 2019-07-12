from rest_framework import serializers

from incidences.models import Incidence

class IncidenceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incidence
        fields = [
            'peritraumatic_fear',
            'injury',
            'rape_type',
            'memory_of_rape',
            'perpetrator_intimate_partner',
            'perpetrator_a_stranger',
            'prior_rape_history',
            'history_of_previous_rape',
            'investigator',
        ]

class IncidenceModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incidence
        fields = [
            'peritraumatic_fear',
            'injury',
            'rape_type',
            'memory_of_rape',
            'perpetrator_intimate_partner',
            'perpetrator_a_stranger',
            'prior_rape_history',
            'history_of_previous_rape',
            'investigator',
        ]