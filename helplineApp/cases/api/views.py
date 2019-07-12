from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from cases.models import Case

from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import CaseModelSerializer, CaseModelUpdateSerializer

class CaseApiListView(generics.ListAPIView):

    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = CaseModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Case.objects.all()
        victim = self.request.GET.get("victim", None)
        perpetrator = self.request.GET.get("perpetrator", None)
        reported_case = self.request.GET.get("reported_case", None)
        location = self.request.GET.get("location", None)
        reported_to = self.request.GET.get("reported_to", None)
        case_no = self.request.GET.get("case_no", None)
        lawyer = self.request.GET.get("lawyer", None)
        police_station = self.request.GET.get("police_station", None)
        court = self.request.GET.get("court", None)
        
        if victim is not None:
            qs = qs.filter(
                Q(victim__icontains=victim) 
                )
        if perpetrator is not None:
            qs = qs.filter(
                Q(perpetrator__icontains=perpetrator) 
                )
        if reported_case is not None:
            qs = qs.filter(
                Q(reported_case__icontains=reported_case) 
                )
        if location is not None:
            qs = qs.filter(
                Q(location__icontains=location) 
                )
        if reported_to  is not None:
            qs = qs.filter(
                Q(reported_to__iexact=reported_to) 
                )
        if case_no  is not None:
            qs = qs.filter(
                Q(case_no__iexact=case_no) 
                )
        if lawyer  is not None:
            qs = qs.filter(
                Q(lawyer__iexact=lawyer) 
                )
        if police_station  is not None:
            qs = qs.filter(
                Q(police_station__iexact=police_station) 
                )
        if court  is not None:
            qs = qs.filter(
                Q(court__iexact=court) 
                )
        return qs


class CaseAPICreateView(generics.CreateAPIView):

    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = CaseModelSerializer
    # permission_classes = [permissions.IsInvestigator]


class CaseApiDetailView(generics.RetrieveAPIView):

    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Case.objects.all()
    serializer_class = CaseModelSerializer


class CaseApiDestroyView(generics.DestroyAPIView):

    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Case.objects.all()
    serializer_class = CaseModelSerializer
    # permission_classes = [permissions.IsAdminUser]


class CaseApiUpdateView(generics.UpdateAPIView):

    authentication_classes = (JSONWebTokenAuthentication, )
    queryset = Case.objects.all()
    serializer_class = CaseModelUpdateSerializer
    # permission_classes = [permissions.IsAdminUser]