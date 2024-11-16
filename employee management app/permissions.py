from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    """
    Custom permission to only allow users with the "admin" role to delete objects.
    """

    def has_permission(self, request, view):
        # Allow other requests if they are not DELETE
        if request.method != 'DELETE':
            return True

        # Check if the user is authenticated and has the "admin" role
        return request.user.is_authenticated and request.user.role == 'admin'
