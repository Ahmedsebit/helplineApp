"""helplineApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/victims/', include(('victims.api.urls', 'victims_api'), namespace='victims-api')),
    path('api/perpetrators/', include(('perpetrators.api.urls', 'perpetrators_api'), namespace='perpetrators-api')),
    path('api/reports/', include(('reports.api.urls', 'reports_api'), namespace='reports-api')),
    path('api/cases/', include(('cases.api.urls', 'cases_api'), namespace='cases-api')),
    path('api/incidences/', include(('incidences.api.urls', 'incidences_api'), namespace='incidences-api')),
    path('api/users/', include(('users.api.urls', 'users_api'), namespace='users-api')),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
