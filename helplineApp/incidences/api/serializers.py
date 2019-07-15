from rest_framework import serializers

from incidences.models import Incidence

class IncidenceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incidence
        fields = [
            'reported_case',
            'peritraumatic_fear',
            'injury',
            'rape_type',
            'memory_of_rape',
            'perpetrator_intimate_partner',
            'perpetrator_a_stranger',
            'prior_rape_history',
            'history_of_previous_rape',
            'reported_case',
            'victim',
            'perpetrator',
            'investigator',
        ]

class IncidenceModelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incidence
        fields = [
            'reported_case',
            'peritraumatic_fear',
            'injury',
            'rape_type',
            'memory_of_rape',
            'perpetrator_intimate_partner',
            'perpetrator_a_stranger',
            'prior_rape_history',
            'history_of_previous_rape',
            'reported_case',
            'victim',
            'perpetrator',
            'investigator',
        ]