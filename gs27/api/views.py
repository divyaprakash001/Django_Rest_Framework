from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  # authentication_classes = [SessionAuthentication]
  # permission_classes = [permissions.DjangoModelPermissions]
