from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "Власник"


class IsWorker(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "Працівник"
