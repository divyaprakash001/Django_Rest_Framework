from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def createStudent(request):
    if request.method == 'GET':
      id = request.data['id']
      student = Student.objects.get(id=id)
      serializer = StudentSerializer(student)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
      serializer = StudentSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Data Inserted', 'dataa':serializer.data}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
  def get(self,request,*args, **kwargs):
    try:
      json_data = request.body
      if json_data:
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id', None)
        if id is not None:
          student = Student.objects.get(id=id)
          serializer = StudentSerializer(student)
          return JsonResponse(serializer.data, safe=False)
        else:
          res = {'msg':'Please give student id to get specific student or blank body to get all students'}
        return JsonResponse(res,safe=False)

      # else part if json data is not passed
      student = Student.objects.all()
      serializer = StudentSerializer(student,many=True)
      return JsonResponse(serializer.data,safe=False)

    except Student.DoesNotExist:
      res = {'msg':"Student Does not exist"}
      return JsonResponse(res,safe=False)
    except :
      res = {'msg':"Something went wrong!"}
      return JsonResponse(res,safe=False)
  

  def post(self,request,*args, **kwargs):
    try:
      json_data = request.body
      stream = io.BytesIO(json_data)
      py_data = JSONParser().parse(stream)
      serializer=StudentSerializer(data = py_data)
      if serializer.is_valid():
        serializer.save()
        res = {'msg':'Data Inserted'}
        json_res = JSONRenderer().render(res)
        return HttpResponse(json_res,content_type='application/json')
      return JsonResponse(serializer.errors, safe=False)
    except :
      res = {'msg':"Something went wrong!"}
      return JsonResponse(res,safe=False)



  def put(self,request,*args, **kwargs):
    try:
      json_data = request.body
      stream  = io.BytesIO(json_data)
      py_data = JSONParser().parse(stream)
      id = py_data.get('id',None)
      if id is not None:
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=py_data,partial=True)
        if serializer.is_valid():
          serializer.save()
          res = {'msg':"Student Updated Completly"}
          json_res = JSONRenderer().render(res)
          return HttpResponse(json_res, content_type='application/json')
        else:
          json_res = JSONRenderer().render(serializer.errors)
          return HttpResponse(json_res, content_type='application/json')
      else:
        res = {'msg':"Id is required"}
        json_res = JSONRenderer().render(res)
        return HttpResponse(json_res, content_type='application/json')
    except Student.DoesNotExist:
      res = {'msg':"Student Does not exist"}
      return JsonResponse(res,safe=False)
    except :
      res = {'msg':"Something went wrong!"}
      return JsonResponse(res,safe=False)


  def delete(self,request,*args, **kwargs):
    try:
      json_data = request.body
      stream  = io.BytesIO(json_data)
      py_data = JSONParser().parse(stream)
      id = py_data.get('id')
      if id is not None:
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg':"Student Deleted !!"}
        return JsonResponse(res, safe=False)
      else:
        res = {'msg':"Id is required"}
        return JsonResponse(res,safe=False)
    except Student.DoesNotExist:
      res = {'msg':"Student Does not exist"}
      return JsonResponse(res,safe=False)
    except :
      res = {'msg':"Something went wrong!"}
      return JsonResponse(res,safe=False)





