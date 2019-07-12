from rest_framework.permissions import BasePermission

class IsAllowedToAddIncidence(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 1 or request.user.user_type == 2

class IsAllowedToAddCase(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 1 or request.user.user_type == 3

class IsAllowedToAddUsers(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 1

