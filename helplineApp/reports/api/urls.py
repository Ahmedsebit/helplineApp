from django.conf.urls import url
from .views import ReportApiListView,  ReportAPICreateView, ReportApiDetailView

urlpatterns = [
    url(r'^$', ReportApiListView.as_view(), name='report'),
    url(r'^create/$', ReportAPICreateView.as_view(), name='report_create'),
    url(r'^(?P<pk>\d+)/$', ReportApiDetailView.as_view(), name='report_detail'),
]