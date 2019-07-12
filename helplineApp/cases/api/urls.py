from django.conf.urls import url
from .views import CaseApiListView,  CaseAPICreateView, CaseApiDetailView, CaseApiDestroyView, CaseApiUpdateView

urlpatterns = [
    url(r'^$', CaseApiListView.as_view(), name='case'),
    url(r'^create/$', CaseAPICreateView.as_view(), name='case_create'),
    url(r'^(?P<pk>\d+)/$', CaseApiDetailView.as_view(), name='case_detail'),
    url(r'^(?P<pk>\d+)/update/$', CaseApiUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', CaseApiDestroyView.as_view(), name='delete'),
]