from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def createStudent(request,id=None):
#   try:
#     if request.method == 'GET':
#       pk = request.data.get('id') if request.data.get('id') else id
#       if pk is not None:
#         try:
#           id_int = int(pk)
#           student = Student.objects.get(id=id_int)
#           serializer = StudentSerializer(student)
#           return Response(serializer.data, status=status.HTTP_200_OK)
#         except ValueError:
#           return Response({'msg':'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
#         # all student data
#       else:
#         student = Student.objects.all()
#         serializer = StudentSerializer(student,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#       serializer = StudentSerializer(data=request.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response({'msg':'Data Inserted', 'dataa':serializer.data}, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     # updating the data
#     elif request.method == 'PUT':
#       pk = request.data.get('id') if request.data.get('id') else id
#       if pk is not None:
#         try:
#           id_int = int(pk)
#           student = Student.objects.get(id=id_int)
#           serializer = StudentSerializer(student,data=request.data)
#           if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Updated successfully'}, status=status.HTTP_200_OK)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except ValueError:
#           return Response({'msg':'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
#       else:
#         return Response({'msg':'ID is Required!'},status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PATCH':
#       pk = request.data.get('id') if request.data.get('id') else id
#       if pk is not None:
#         try:
#           id_int = int(pk)
#           student = Student.objects.get(id=id_int)
#           serializer = StudentSerializer(student,data=request.data,partial=True)
#           if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Updated successfully'}, status=status.HTTP_200_OK)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except ValueError:
#           return Response({'msg':'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
#       else:
#         return Response({'msg':'ID is Required!'},status=status.HTTP_400_BAD_REQUEST)
      
        
#     elif request.method == 'DELETE':
#       pk = request.data.get('id') if request.data.get('id') else id
#       if pk is not None:
#         try:
#           id_int = int(pk)
#           student = Student.objects.get(id=id_int)
#           student.delete()
#           res = {'msg':"Student Deleted !!"}
#           return JsonResponse(res, safe=False)
#         except ValueError:
#           return Response({'msg':'Invalid Id. Give numeric value'}, status=status.HTTP_400_BAD_REQUEST)
#       else:
#         return Response({'msg':'ID required.'}, status=status.HTTP_400_BAD_REQUEST)
        
#   except Student.DoesNotExist:
#     return Response({'msg':'Student Does not exists.'}, status=status.HTTP_404_NOT_FOUND)
#   except:
#     return Response({'msg':"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)




@method_decorator(csrf_exempt, name='dispatch')
class StudentAPIView(APIView):
  def get(self,request,id=None,format=None):
    try:
      pk = request.data.get('id') if request.data.get('id') else id
      if pk is not None:
        try:
          id_int = int(pk)
          student = Student.objects.get(id=id_int)
          serializer = StudentSerializer(student)
          return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
          return Response({'msg':'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
        # all student data
      else:
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Student.DoesNotExist:
      return Response({'msg':'Student Does not exists.'}, status=status.HTTP_404_NOT_FOUND)
    except:
      return Response({'msg':"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
  

  def post(self,request,format=None):
    try:
      serializer = StudentSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Data Inserted', 'dataa':serializer.data}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
      return Response({'msg':"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)



  def put(self,request,id=None,format=None):
    try:
      pk = request.data.get('id') if request.data.get('id') else id
      if pk is not None:
        try:
          id_int = int(pk)
          student = Student.objects.get(id=id_int)
          serializer = StudentSerializer(student,data=request.data)
          if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Updated successfully'}, status=status.HTTP_200_OK)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
          return Response({'msg':'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({'msg':'ID is Required!'},status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
      return Response({'msg':'Student Does not exists.'}, status=status.HTTP_404_NOT_FOUND)
    except:
      return Response({'msg':"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

  def patch(self,request,id=None,format=None):
    try:
      pk = request.data.get('id') if request.data.get('id') else id
      if pk is not None:
        try:
          id_int = int(pk)
          student = Student.objects.get(id=id_int)
          serializer = StudentSerializer(student,data=request.data, partial=True)
          if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Updated successfully'}, status=status.HTTP_200_OK)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
          return Response({'msg':'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({'msg':'ID is Required!'},status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
      return Response({'msg':'Student Does not exists.'}, status=status.HTTP_404_NOT_FOUND)
    except:
      return Response({'msg':"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


  def delete(self,request,id=None,format=None):
    try:
      pk = request.data.get('id') if request.data.get('id') else id
      if pk is not None:
        try:
          id_int = int(pk)
          student = Student.objects.get(id=id_int)
          student.delete()
          res = {'msg':"Student Deleted !!"}
          return JsonResponse(res, safe=False)
        except ValueError:
          return Response({'msg':'Invalid Id. Give numeric value'}, status=status.HTTP_400_BAD_REQUEST)
      else:
        return Response({'msg':'ID required.'}, status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
      return Response({'msg':'Student Does not exists.'}, status=status.HTTP_404_NOT_FOUND)
    except:
      return Response({'msg':"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)





