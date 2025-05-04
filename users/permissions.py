from rest_framework.permissions import BasePermission




class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False 
        role = request.user.role
        if role.lower() == 'doctor':
            return True
        else:
            return False
    def has_object_permission(self, request, view, obj):
        if obj.patient.created_by == request.user:
            return True
        else:
            return False

