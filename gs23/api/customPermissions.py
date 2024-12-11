from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):

  def has_permission(self, request, view):
    if request.user.is_staff == True:
      return True
    return False