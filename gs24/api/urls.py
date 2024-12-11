from django.urls import path,include
from . import views

urlpatterns = [
    path('studentapi/',views.createStudent, name="studentApi"),
    path('studentapi/<id>/',views.createStudent,  name="studentApi"),
    path('auth/',include('rest_framework.urls')),
]
