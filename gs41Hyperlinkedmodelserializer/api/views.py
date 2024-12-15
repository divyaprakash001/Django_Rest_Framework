from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer






class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer




 