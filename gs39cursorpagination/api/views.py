from requests import Response
from rest_framework.generics import ListAPIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, CursorPagination
from .myPaginator import MyPagination





class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'scoping'
  filter_backends = [SearchFilter,OrderingFilter]
  search_fields = ['^name','roll','city','passby']
  ordering_fields = ['name','city']
  # pagination_class = CursorPagination  #must have created field in models
  pagination_class = MyPagination




 