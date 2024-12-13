from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import DestroyAPIView,CreateAPIView,ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.throttling import ScopedRateThrottle
# create 
class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'

# list
class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'viewstu'

  # retrieve
class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'viewstu'

  # update
class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'

  # delete
class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'



