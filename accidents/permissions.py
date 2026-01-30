from rest_framework import permissions

class IsAdminOrNoDelete(permissions.BasePermission):
    """
    Custom permission to only allow Admins to delete objects.
    Personnel can View (GET) and Add (POST), but NOT Delete.
    """
    def has_permission(self, request, view):
        # We already know they are logged in because of settings.py
        # Check if they are trying to DELETE
        if request.method == 'DELETE':
            # Only allow if they are an Admin (is_staff)
            return request.user.is_staff
        
        # For GET, POST, PUT, PATCH -> Allow everyone who is logged in
        return True