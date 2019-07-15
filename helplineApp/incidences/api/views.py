from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from incidences.models import Incidence
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import IncidenceModelSerializer, IncidenceModelUpdateSerializer
from users.permissions import IsAllowedToAddIncidences
class IncidenceApiListView(generics.ListAPIView):

    serializer_class = IncidenceModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddIncidences]

    def get_queryset(self, *args, **kwargs):
        
        qs = Incidence.objects.all()

        peritraumatic_fear = self.request.GET.get('peritraumatic_fear', None)
        injury = self.request.GET.get('injury', None)
        rape_type = self.request.GET.get('rape_type', None)
        memory_of_rape = self.request.GET.get('memory_of_rape', None)
        perpetrator_intimate_partner = self.request.GET.get('perpetrator_intimate_partner', None)
        perpetrator_a_stranger = self.request.GET.get('perpetrator_a_stranger', None)
        prior_rape_history = self.request.GET.get('prior_rape_history', None)
        history_of_previous_rape = self.request.GET.get('history_of_previous_rape', None)
        investigator = self.request.GET.get('investigator', None)
    
        if peritraumatic_fear is not None:
            qs = qs.filter(
                Q(peritraumatic_fear__icontains=peritraumatic_fear) 
                )
        if injury is not None:
            qs = qs.filter(
                Q(injury__icontains=injury) 
                )
        if rape_type is not None:
            qs = qs.filter(
                Q(rape_type__icontains=rape_type) 
                )
        if memory_of_rape is not None:
            qs = qs.filter(
                Q(memory_of_rape__icontains=memory_of_rape) 
                )
        if perpetrator_intimate_partner is not None:
            qs = qs.filter(
                Q(perpetrator_intimate_partner__iexact=perpetrator_intimate_partner) 
                )
        if perpetrator_a_stranger is not None:
            qs = qs.filter(
                Q(perpetrator_a_stranger__iexact=perpetrator_a_stranger) 
                )
        if prior_rape_history is not None:
            qs = qs.filter(
                Q(prior_rape_history__iexact=prior_rape_history) 
                )
        if history_of_previous_rape is not None:
            qs = qs.filter(
                Q(history_of_previous_rape__iexact=history_of_previous_rape) 
                )
        if investigator is not None:
            qs = qs.filter(
                Q(investigator__iexact=investigator) 
                )
        return qs


class IncidenceAPICreateView(generics.CreateAPIView):

    serializer_class = IncidenceModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddIncidences]


class IncidenceApiDetailView(generics.RetrieveAPIView):

    serializer_class = IncidenceModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddIncidences]
    queryset = Incidence.objects.all()


class IncidenceApiDestroyView(generics.DestroyAPIView):

    serializer_class = IncidenceModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddIncidences]
    queryset = Incidence.objects.all()


class IncidenceApiUpdateView(generics.UpdateAPIView):

    serializer_class = IncidenceModelUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddIncidences]
    queryset = Incidence.objects.all()