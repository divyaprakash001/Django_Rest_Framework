from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
  id= serializers.IntegerField(read_only=True)
  name = serializers.CharField(max_length=50)
  roll=serializers.IntegerField()
  city = serializers.CharField(max_length=50)

  def create(self,validate_data):
    return Student.objects.create(**validate_data)