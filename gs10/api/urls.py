from django.urls import path,include
from . import views

urlpatterns = [
    path('studentApi/',views.createStudent, name="studentApi"),
]
