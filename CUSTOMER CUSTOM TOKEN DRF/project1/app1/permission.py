from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGet_Post_Pit(BasePermission):
    def has_permission(self, request, view):
        allowed_method = ['GET', 'POST', 'PUT']
        if request.method in allowed_method:
            return True
        else:
            return True

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_authenticated
        if status == True:
            allowed_method = ['GET', 'POST', 'PUT', 'DELETE']
            if request.method in allowed_method:
                return True
            else:
                return False
        else:
            if request.method in SAFE_METHODS:
                return True
            return False

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_superuser
        if status == True:
            allowed_method = ['GET', 'POST', 'PUT', 'DELETE']
            if request.method in allowed_method:
                return True
            else:
                return False
        else:
            if request.method in SAFE_METHODS:
                return True
            return False

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        status = request.user.is_staff
        if status == True:
            allowed_method = ['GET', 'POST', 'PUT', 'DELETE']
            if request.method in allowed_method:
                return True
            else:
                return False
        else:
            if request.method in SAFE_METHODS:
                return True
            return False