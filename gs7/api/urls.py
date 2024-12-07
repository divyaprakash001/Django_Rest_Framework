from django.urls import path,include
from . import views

urlpatterns = [
    path('studentApi/',views.StudentAPI.as_view(), name="studentApi"),
]
