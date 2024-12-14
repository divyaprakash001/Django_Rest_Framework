from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle, ScopedRateThrottle
from .throttling import MyThrottling
from rest_framework.response import Response



# Create your views here.


class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  # throttle_classes = [AnonRateThrottle,UserRateThrottle]
  # throttle_classes = [AnonRateThrottle,MyThrottling]
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'scoping'

  def get_queryset(self):
    try:
      return Student.objects.filter(passby = self.request.user)
    except:
      return Response({'msg':"Something got wrong"})


  # def get_queryset(self):
  #   name = self.request.data.get('name',None)
  #   roll = self.request.data.get('roll',None)
  #   city = self.request.data.get('city',None)
  #   passby = self.request.data.get('passby',None)
  #   conditions = {}
  #   if name is not None and name is not '':
  #     conditions['name__icontains'] = name
  #   if roll is not None and roll is not '':
  #     conditions['roll'] = roll
  #   if city is not None and city is not '':
  #     conditions['city__icontains'] = city
  #   if passby is not None and passby is not '':
  #     conditions['passby__icontains'] = passby
  #   # print(self.request.data)
  #   return Student.objects.filter(**)