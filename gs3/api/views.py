from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def studentApi(request):
  try:
    if request.method == 'GET':
      json_data = request.body
      if json_data:
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id', None)
        if id is not None:
          student = Student.objects.get(id=id)
          serializer = StudentSerializer(student)
          # json_res_data = JSONRenderer().render(serializer.data)
          return JsonResponse(serializer.data, safe=False)
        else:
          res = {'msg':'Please give student id to get specific student or blank body to get all students'}
        # json_res = JSONRenderer().render(res)
        return JsonResponse(res,safe=False)

        
      student = Student.objects.all()
      serializer = StudentSerializer(student,many=True)
      # json_res_data = JSONRenderer().render(serializer.data)
      return JsonResponse(serializer.data,safe=False)


    elif request.method == 'POST':
      json_data = request.body
      stream = io.BytesIO(json_data)
      py_data = JSONParser().parse(stream)
      serializer=StudentSerializer(data = py_data)
      if serializer.is_valid():
        serializer.save()
        res = {'msg':'Data Inserted'}
        json_res = JSONRenderer().render(res)
        return HttpResponse(json_res,content_type='application/json')
      res = {'msg':'Data Insertion Failed'}
      return JsonResponse(serializer.errors, safe=False)


    elif request.method == 'PUT':
      json_data = request.body
      stream  = io.BytesIO(json_data)
      py_data = JSONParser().parse(stream)
      id = py_data.get('id')
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

        
    elif request.method == 'DELETE':
      json_data = request.body
      stream  = io.BytesIO(json_data)
      py_data = JSONParser().parse(stream)
      id = py_data.get('id')
      if id is not None:
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg':"Student Deleted !!"}
        json_res = JSONRenderer().render(res)
        return HttpResponse(json_res, content_type='application/json')
      else:
        res = {'msg':"Id is required"}
        json_res = JSONRenderer().render(res)
        return HttpResponse(json_res, content_type='application/json')

  except Student.DoesNotExist:
    res = {'msg':"Data Does not exist"}
    json_res = JSONRenderer().render(res)
    return HttpResponse(json_res, content_type='application/json')
  

@csrf_exempt
def updateStudent(request):
  try:
    if request.method == 'PUT':
      json_data = request.body
      stream  = io.BytesIO(json_data)
      py_data = JSONParser().parse(stream)
      id = py_data.get('id')
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
    else:
      res = {'msg':"Request method not allowed"}
      json_res = JSONRenderer().render(res)
      return HttpResponse(json_res, content_type='application/json')

  except Student.DoesNotExist:
    res = {'msg':"Student Does not exist"}
    json_res = JSONRenderer().render(res)
    return HttpResponse(json_res, content_type='application/json')
