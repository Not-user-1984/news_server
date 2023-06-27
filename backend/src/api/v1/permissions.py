from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)


class AllowAnyReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        elif request.method in ['POST'] and view.action in ['like', 'unlike']:
            return True
        elif request.user and request.user.is_authenticated:
            return True
        else:
            return False
