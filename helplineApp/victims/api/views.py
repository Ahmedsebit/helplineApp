from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from victims.models import Victim
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import VictimModelSerializer, VictimModelUpdateSerializer

class VictimApiListView(generics.ListAPIView):

    serializer_class = VictimModelSerializer

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
    # permission_classes = [permissions.IsAdminUser]


class VictimApiDetailView(generics.RetrieveAPIView):

    queryset = Victim.objects.all()
    serializer_class = VictimModelSerializer


class VictimApiDestroyView(generics.DestroyAPIView):

    queryset = Victim.objects.all()
    serializer_class = VictimModelSerializer
    # permission_classes = [permissions.IsAdminUser]


class VictimApiUpdateView(generics.UpdateAPIView):

    queryset = Victim.objects.all()
    serializer_class = VictimModelUpdateSerializer
    # permission_classes = [permissions.IsAdminUser]