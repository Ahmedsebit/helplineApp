from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser

from .serializers import UserDisplaySerializer, UserSerializer, UserUpdateSerializer

from users.permissions import IsAllowedToAddUsers
from users.models import User


class UserApiCreateView(generics.CreateAPIView):

    serializer_class = UserDisplaySerializer

    permission_classes = [permissions.IsAuthenticated, IsAllowedToAddUsers]
    # authentication_classes = (JSONWebTokenAuthentication, )
    

class UserApiDetailListView(generics.ListAPIView):

    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JSONWebTokenAuthentication, )

    def get_queryset(self, *args, **kwargs):
        qs = User.objects.filter(id=self.request.user.id)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(username__icontains=query) 
                )
        return qs


class CustomUserApiDetailView(generics.RetrieveAPIView):

    serializer_class = UserSerializer
    
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JSONWebTokenAuthentication, )
    
    queryset = User.objects.all()
    

class CustomUserApiDestroyView(generics.DestroyAPIView):

    serializer_class = UserSerializer
    
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    

class UserApiUpdateView(generics.UpdateAPIView):

    serializer_class = UserUpdateSerializer

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JSONWebTokenAuthentication, )

    queryset = User.objects.all()
    