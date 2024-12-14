from rest_framework.generics import ListAPIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend





class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'scoping'
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['name','city']

  # def get_queryset(self):
  #   try:
  #     return Student.objects.filter(passby = self.request.user)
  #   except:
  #     return Response({'msg':"Something got wrong"})


 