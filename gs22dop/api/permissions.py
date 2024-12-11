# api/permissions.py
from guardian.shortcuts import assign_perm
from rest_framework.permissions import BasePermission

class IsStudentOwner(BasePermission):
    """
    Custom permission to allow users to view/edit only their own student record.
    """
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is the owner (i.e., the student belongs to this teacher)
        return obj.teacher.user == request.user
