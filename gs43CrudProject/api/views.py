from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer

from .models import User

# Create your views here.
class UserModelViewset(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer