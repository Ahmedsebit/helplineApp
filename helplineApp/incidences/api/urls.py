from django.conf.urls import url
from .views import IncidenceApiListView,  IncidenceAPICreateView, IncidenceApiDetailView, IncidenceApiDestroyView, IncidenceApiUpdateView

urlpatterns = [
    url(r'^$', IncidenceApiListView.as_view(), name='incidence'),
    url(r'^create/$', IncidenceAPICreateView.as_view(), name='incidence_create'),
    url(r'^(?P<pk>\d+)/$', IncidenceApiDetailView.as_view(), name='incidence_detail'),
    url(r'^(?P<pk>\d+)/update/$', IncidenceApiUpdateView.as_view(), name='incidence_update'),
    url(r'^(?P<pk>\d+)/delete/$', IncidenceApiDestroyView.as_view(), name='incidence_delete'),
]