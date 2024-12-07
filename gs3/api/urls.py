from django.urls import path,include
from . import views

urlpatterns = [
    path('studentApi/',views.studentApi, name="studentApi"),
    path('updateStudent/',views.updateStudent, name="updateStudent"),
]
