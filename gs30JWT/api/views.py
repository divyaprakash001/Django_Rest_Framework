from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [JWTAuthentication]
  permission_classes = [permissions.IsAuthenticated]
