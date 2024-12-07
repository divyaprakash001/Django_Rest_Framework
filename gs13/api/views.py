from .models import Student
from .serializer import StudentSerializer
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView

# list and create - PK Not Required
class StudentListCreate(GenericAPIView, CreateModelMixin, ListModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self,request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self,request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


# list and create - PK Not Required
class StudentRUDList(GenericAPIView, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self,request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self,request, *args, **kwargs):
    return self.update(request, *args, **kwargs)
  
  def patch(self,request, *args, **kwargs):
    return self.update(request, *args, **kwargs)
  
  def delete(self,request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)


