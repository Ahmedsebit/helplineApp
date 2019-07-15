from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser

from django.db.models import Q
from victims.models import Victim

from .serializers import VictimModelSerializer, VictimModelUpdateSerializer

from users.permissions import IsAllowedToAddVictims
class VictimApiListView(generics.ListAPIView):

    serializer_class = VictimModelSerializer

    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddVictims]

    def get_queryset(self, *args, **kwargs):
        qs = Victim.objects.all()
        first_name = self.request.GET.get("first_name", None)
        last_name = self.request.GET.get("last_name", None)
        middle_name = self.request.GET.get("middle_name", None)
        location = self.request.GET.get("location", None)
        date = self.request.GET.get("date", None)
        
        if first_name is not None:
            qs = qs.filter(
                Q(first_name__icontains=first_name) 
                )
        if last_name is not None:
            qs = qs.filter(
                Q(first_name__icontains=first_name) 
                )
        if middle_name is not None:
            qs = qs.filter(
                Q(first_name__icontains=first_name) 
                )
        if location is not None:
            qs = qs.filter(
                Q(location__icontains=location) 
                )
        if date is not None:
            qs = qs.filter(
                Q(date__iexact=date) 
                )
        return qs


class VictimAPICreateView(generics.CreateAPIView):

    serializer_class = VictimModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddVictims]


class VictimApiDetailView(generics.RetrieveAPIView):

    serializer_class = VictimModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddVictims]
    queryset = Victim.objects.all()

class VictimApiDestroyView(generics.DestroyAPIView):

    serializer_class = VictimModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddVictims]
    queryset = Victim.objects.all()


class VictimApiUpdateView(generics.UpdateAPIView):

    serializer_class = VictimModelUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddVictims]
    queryset = Victim.objects.all()