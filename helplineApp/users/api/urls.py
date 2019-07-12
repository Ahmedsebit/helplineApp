from django.conf.urls import url
from .views import UserApiCreateView, UserApiUpdateView, UserApiDetailListView

urlpatterns = [
    url(r'^$', UserApiDetailListView.as_view(), name='user_list'),
    url(r'^create/$', UserApiCreateView.as_view(), name='user_create'),
    url(r'^(?P<pk>\d+)/update/$', UserApiUpdateView.as_view(), name='user_update'),
]