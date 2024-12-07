from rest_framework import serializers

from .models import Student

# validators #high priority
def start_with_z(value):
  if value[0].lower() != 'z':
    raise serializers.ValidationError("Name should start with z")
  

class StudentSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(read_only=True)
  name=serializers.CharField(max_length=50, validators=[start_with_z], read_only=True)

  class Meta:
    model = Student
    fields = ['id','name', 'roll', 'city']
    # fields='__all__'
    # exclude = ['roll']
    # read_only_fields = ['id','name']
    # extra_kwargs = {'name':{'ready_only':True}}

# field level validation
  def validate_roll(self,value):
    if Student.objects.filter(roll=value).exists():
      raise serializers.ValidationError("This roll number is already taken.")
    return value
  
  # object level validation
  def validate(self, data): # data is dictionary
      
    if Student.objects.count() >= 105:
      raise serializers.ValidationError("Admission limit reached. Only 105 students are allowed.")
    
    return data
