from rest_framework import serializers
from .models import Student  # Assuming your model is named Student

class StudentSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  name = serializers.CharField(max_length=50)
  roll = serializers.IntegerField()
  city = serializers.CharField(max_length=50)

# jisko serialize krna hai usi ko yaha likhenge


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']  # Explicitly specify the fields you want to include
