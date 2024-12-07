from django.urls import path
from . import views
urlpatterns = [
    path("allStudents/",views.allStudents, name="allStudents"),
    path("addStudent/",views.addStudent, name="addStudent"),

]
