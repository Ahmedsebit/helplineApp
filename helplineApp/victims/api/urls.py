from django.conf.urls import url
from .views import VictimApiListView,  VictimAPICreateView, VictimApiDetailView, VictimApiDestroyView, VictimApiUpdateView

urlpatterns = [
    url(r'^$', VictimApiListView.as_view(), name='victim'),
    url(r'^create/$', VictimAPICreateView.as_view(), name='victim_create'),
    url(r'^(?P<pk>\d+)/$', VictimApiDetailView.as_view(), name='victim_detail'),
    url(r'^(?P<pk>\d+)/update/$', VictimApiUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', VictimApiDestroyView.as_view(), name='delete')
]