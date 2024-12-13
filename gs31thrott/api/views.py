from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import JackRateThrottle


class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  # throttle_classes = [AnonRateThrottle, UserRateThrottle]
  throttle_classes = [AnonRateThrottle, JackRateThrottle]
