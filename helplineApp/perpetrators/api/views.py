from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from perpetrators.models import Perpetrator
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import PerpetratorModelSerializer, PerpetratorModelUpdateSerializer
from users.permissions import IsAllowedToAddPerpetrators
class PerpetratorApiListView(generics.ListAPIView):

    serializer_class = PerpetratorModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddPerpetrators]

    def get_queryset(self, *args, **kwargs):
        qs = Perpetrator.objects.all()
        first_name = self.request.GET.get("first_name", None)
        last_name = self.request.GET.get("last_name", None)
        middle_name = self.request.GET.get("middle_name", None)
        location = self.request.GET.get("location", None)
        national_id_number = self.request.GET.get("national_id_number", None)
        
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
        if national_id_number is not None:
            qs = qs.filter(
                Q(national_id_number__iexact=national_id_number) 
                )
        return qs


class PerpetratorAPICreateView(generics.CreateAPIView):

    serializer_class = PerpetratorModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddPerpetrators]
    queryset = Perpetrator.objects.all()


class PerpetratorApiDetailView(generics.RetrieveAPIView):

    serializer_class = PerpetratorModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddPerpetrators]
    queryset = Perpetrator.objects.all()


class PerpetratorApiDestroyView(generics.DestroyAPIView):

    serializer_class = PerpetratorModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddPerpetrators]
    queryset = Perpetrator.objects.all()


class PerpetratorApiUpdateView(generics.UpdateAPIView):

    serializer_class = PerpetratorModelUpdateSerializer  
    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddPerpetrators]
    queryset = Perpetrator.objects.all()