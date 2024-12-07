from django.urls import path
from . import views

urlpatterns = [
    path("studentDetail/<pk>/",views.student_detail, name="studentDetail"),
    path("allStudents/",views.allStudents, name="allStudents"),
    path("addStudent/",views.addStudent, name="addStudent"),
]
