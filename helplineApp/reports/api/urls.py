from django.conf.urls import url
from .views import ReportApiListView,  ReportAPICreateView, ReportApiDetailView, ReportApiDestroyView, ReportApiUpdateView

urlpatterns = [
    url(r'^$', ReportApiListView.as_view(), name='report'),
    url(r'^create/$', ReportAPICreateView.as_view(), name='report_create'),
    url(r'^(?P<pk>\d+)/$', ReportApiDetailView.as_view(), name='report_detail'),
    url(r'^(?P<pk>\d+)/update/$', ReportApiUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ReportApiDestroyView.as_view(), name='delete')
]