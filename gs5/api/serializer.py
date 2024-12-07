from rest_framework import serializers

from .models import Student

# validators #high priority
def start_with_z(value):
  if value[0].lower() != 'z':
    raise serializers.ValidationError("Name should start with z")
  

class StudentSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  name=serializers.CharField(max_length=50, validators=[start_with_z])
  roll=serializers.IntegerField()
  city=serializers.CharField(max_length=50)

  def create(self, validated_data):
    if Student.objects.count() >= 105:
      raise serializers.ValidationError("Admission limit reached. Only 35 students are allowed.")
    return Student.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    # print(instance.name)
    instance.name = validated_data.get('name',instance.name)
    # print(instance.name)
    instance.roll = validated_data.get('roll',instance.roll)
    instance.city = validated_data.get('city',instance.city)
    instance.save()
    return instance
  
  # this method is automatically invoked when is_valid() is called
  # then field level validation priority
  def validate_roll(self,value):
    if value >= 200:
      raise serializers.ValidationError("Seat Full")
    return value
  
  # then object level validation priority 
  def validate(self, data): # data is dictionary
    roll = data.get('roll')  
    # last_id = Student.objects.aggregate(max('id'))['id__max']
    # print(last_id)
    if Student.objects.filter(roll=roll).exists():
      raise serializers.ValidationError("This roll number is already taken.")
    if Student.objects.count() >= 105:
      raise serializers.ValidationError("Admission limit reached. Only 35 students are allowed.")
    
    return data
