from rest_framework.permissions import BasePermission


class IsAllowedToAddUsers(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 1


class IsAllowedToAddVictims(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 1 or request.user.user_type == 2


class IsAllowedToAddPerpetrators(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 1 or request.user.user_type == 2


class IsAllowedToAddIncidences(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 1 or request.user.user_type == 2


class IsAllowedToAddCases(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 1 or request.user.user_type == 3