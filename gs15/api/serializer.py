from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(read_only=True)

  class Meta:
    model = Student
    fields = ['id','name', 'roll', 'city']

  def create(self, validated_data):
    return super().create(validated_data)

  # def validate_roll(self,value):
  #   if Student.objects.filter(roll=value).exists():
  #     raise serializers.ValidationError("This roll number is already taken.")
  #   return value
  
  def validate(self, data): 
    if Student.objects.count() >= 105:
      raise serializers.ValidationError("Admission limit reached. Only 105 students are allowed.")
    
    return data
