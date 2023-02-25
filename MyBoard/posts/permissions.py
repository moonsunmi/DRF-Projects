from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    """GET: True
    PUT: 해당 사용자만"""
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # Read Only
            return True
        return obj.user == request.user


