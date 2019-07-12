from django.conf.urls import url
from .views import PerpetratorApiListView,  PerpetratorAPICreateView, PerpetratorApiDetailView, PerpetratorApiDestroyView, PerpetratorApiUpdateView

urlpatterns = [
    url(r'^$', PerpetratorApiListView.as_view(), name='Perpetrator'),
    url(r'^create/$', PerpetratorAPICreateView.as_view(), name='Perpetrator_create'),
    url(r'^(?P<pk>\d+)/$', PerpetratorApiDetailView.as_view(), name='Perpetrator_detail'),
    url(r'^(?P<pk>\d+)/update/$', PerpetratorApiUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', PerpetratorApiDestroyView.as_view(), name='delete'),
]