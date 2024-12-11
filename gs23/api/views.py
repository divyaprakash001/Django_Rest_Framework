from .customPermissions import MyPermission
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [SessionAuthentication]
  # permission_classes = [permissions.DjangoModelPermissions]
  # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
  permission_classes = [MyPermission]
