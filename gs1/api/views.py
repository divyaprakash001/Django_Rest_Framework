from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
from .models import Student
from django.http import HttpResponse,JsonResponse

# Create your views here.
# Model Object - single student data

def student_detail(request,pk):
  stu = Student.objects.get(id=pk)
  # stu = Student.objects.all()
  # print(stu)
  serializer = StudentSerializer(stu)
  # serializer = StudentSerializer(stu,many=True)
  # print(serializer)
  # print(type(serializer.data))
  json_data = JSONRenderer().render(serializer.data)
  # print(json_data)
  # print(type(json_data))
  # print(type(json_data.decode("utf-8")))  #converted to json string 
  return HttpResponse(json_data, content_type='application/json')
  

# def allStudents(request):
#   stu = Student.objects.all()
#   # print(stu)
#   serializer = StudentSerializer(stu,many=True)
#   # print(type(serializer.data))
#   json_data = JSONRenderer().render(serializer.data)
#   print(json_data)
#   return HttpResponse(json_data, content_type='application/json')
  
def allStudents(request):
  stu = Student.objects.all()
  serializer = StudentSerializer(stu,many=True)
  serialized_data = serializer.data
  return JsonResponse(serialized_data, safe=False) 

def addStudent(request):
  if request.method == 'POST':
    print(request.POST) 
  return HttpResponse("hllo") 
  