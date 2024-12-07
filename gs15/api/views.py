from .models import Student
from .serializer import StudentSerializer
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView, DestroyAPIView,CreateAPIView,ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView

# create 
class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

# list
class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  # retrieve
class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  # update
class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  # delete
class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  # retrieve, update, delete
class StudentRUD(RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


