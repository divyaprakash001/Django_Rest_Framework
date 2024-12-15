from requests import Response
from rest_framework import viewsets
from .models import Singer,Song
from .serializer import SingerSerializer,SongSerializer


class SingerViewSet(viewsets.ModelViewSet):
  queryset = Singer.objects.all()
  serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
  queryset = Song.objects.all()
  serializer_class = SongSerializer









 