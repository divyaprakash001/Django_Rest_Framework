from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
