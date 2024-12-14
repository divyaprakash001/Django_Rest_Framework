from . import views
from django.urls import path

urlpatterns = [
    path("studentlist/", views.StudentList.as_view(),name="studentlist"),
]
