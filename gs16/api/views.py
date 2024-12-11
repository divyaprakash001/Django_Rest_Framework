from .models import Student
from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


class StudentViewSet(viewsets.ViewSet):

  def list(self,request):
    print("*************List***********")
    print("Basename : ", self.basename)
    print("Action : ", self.action)
    print("Detail : ", self.detail)
    print("Suffix : ", self.suffix)
    print("Name : ", self.name)
    print("Description : ", self.description)
    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    print("*************Retrieve***********")
    print("Basename : ", self.basename)
    print("Action : ", self.action)
    print("Detail : ", self.detail)
    print("Suffix : ", self.suffix)
    print("Name : ", self.name)
    print("Description : ", self.description)
    id = pk if pk else request.data.get('id')
    if id is not None:
      try:
        id_int = int(id)
        student = Student.objects.get(id=id_int)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
      except ValueError:
        return Response({'msg':"Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
      except Student.DoesNotExist:
        return Response({'msg':"Data Does not exists."}, status=status.HTTP_404_NOT_FOUND)
      except:
        return Response({'msg':"Something got error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  
  def create(self, request):
    print("*************Create***********")
    print("Basename : ", self.basename)
    print("Action : ", self.action)
    print("Detail : ", self.detail)
    print("Suffix : ", self.suffix)
    print("Name : ", self.name)
    print("Description : ", self.description)
    serializer= StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def update(self, request, pk=None):
    print("*************Update***********")
    print("Basename : ", self.basename)
    print("Action : ", self.action)
    print("Detail : ", self.detail)
    print("Suffix : ", self.suffix)
    print("Name : ", self.name)
    print("Description : ", self.description)
    id = pk if pk else request.data.get('id')
    if id is not None:
      try:
        id_int = int(id)
        student = Student.objects.get(id=id_int)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Completly Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      except ValueError:
        return Response({'msg':"Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
      except Student.DoesNotExist:
        return Response({'msg':"Data Does not exists."}, status=status.HTTP_404_NOT_FOUND)
      except:
        return Response({'msg':"Something got error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def partial_update(self, request, pk=None):
    print("*************Partial Update***********")
    print("Basename : ", self.basename)
    print("Action : ", self.action)
    print("Detail : ", self.detail)
    print("Suffix : ", self.suffix)
    print("Name : ", self.name)
    print("Description : ", self.description)
    id = pk if pk else request.data.get('id')
    if id is not None:
      try:
        id_int = int(id)
        student = Student.objects.get(id=id_int)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Partialy Data Updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      except ValueError:
        return Response({'msg':"Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
      except Student.DoesNotExist:
        return Response({'msg':"Data Does not exists."}, status=status.HTTP_404_NOT_FOUND)
      except:
        return Response({'msg':"Something got error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def destroy(self, request, pk=None):
    print("*************Destroy***********")
    print("Basename : ", self.basename)
    print("Action : ", self.action)
    print("Detail : ", self.detail)
    print("Suffix : ", self.suffix)
    print("Name : ", self.name)
    print("Description : ", self.description)
    id = pk if pk else request.data.get('id')
    if id is not None:
      try:
        id_int = int(id)
        student = Student.objects.get(id=id_int)
        student.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)
      except ValueError:
        return Response({'msg':"Invalid ID"}, status=status.HTTP_400_BAD_REQUEST)
      except Student.DoesNotExist:
        return Response({'msg':"Data Does not exists."}, status=status.HTTP_404_NOT_FOUND)
      except:
        return Response({'msg':"Something got error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
