from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from reports.models import Report
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ReportModelSerializer, ReportModelUpdateSerializer

class ReportApiListView(generics.ListAPIView):

    serializer_class = ReportModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Report.objects.all()
        info = self.request.GET.get("info", None)
        report_date = self.request.GET.get("report_date", None)
        case_opened = self.request.GET.get("case_opened", None)
        
        if info is not None:
            qs = qs.filter(
                Q(info_name__icontains=info) 
                )
        if report_date is not None:
            qs = qs.filter(
                Q(report_date__icontains=report_date) 
                )
        if case_opened is not None:
            qs = qs.filter(
                Q(case_opened__icontains=case_opened) 
                )
        return qs


class ReportAPICreateView(generics.CreateAPIView):

    serializer_class = ReportModelSerializer
    # permission_classes = [permissions.IsAdminUser]


class ReportApiDetailView(generics.RetrieveAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportModelSerializer


class ReportApiDestroyView(generics.DestroyAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportModelSerializer
    # permission_classes = [permissions.IsAdminUser]


class ReportApiUpdateView(generics.UpdateAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportModelUpdateSerializer
    # permission_classes = [permissions.IsAdminUser]