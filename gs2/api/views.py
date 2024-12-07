import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .models import Student

# Create your views here.
def allStudents(request):
  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many=True)
  # json_data = JSONRenderer().render(serializer.data)
  # return HttpResponse(json_data,content_type='application/json')
  return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def addStudent(request):
  if request.method == 'POST':
    json_data = request.body
    stream = io.BytesIO(json_data)
    py_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data=py_data)
    if serializer.is_valid():
      serializer.save()
      res = {'msg':'Data Inserted'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')

    json_data =  JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')