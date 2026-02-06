from rest_framework import permissions


class AccidentRolePermission(permissions.BasePermission):
    """
    Role-based permissions for AccidentReport API:

    - Any authenticated user (any role) can READ (GET/HEAD/OPTIONS).
    - Only Admins (is_staff) and Encoder group members can CREATE/UPDATE.
    - Only Admins (is_staff) can DELETE.

    Expected roles (Django groups):
    - 'Encoder'
    - 'Officer'
    Admin is represented by user.is_staff.
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE':
            return user.is_staff

        if user.is_staff:
            return True

        # Encoders can create/update
        return user.groups.filter(name='Encoder').exists()