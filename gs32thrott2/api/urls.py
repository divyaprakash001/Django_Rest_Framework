from django.urls import path
from . import views

urlpatterns = [
    # path('studentApi/',views.createStudent, name="studentApi"),
    path('student/create/',views.StudentCreate.as_view(),  name="createStudent"),
    path('student/list/',views.StudentList.as_view(),  name="studentList"),
    path('student/retrieve/<pk>/',views.StudentRetrieve.as_view(),  name="studentRetrieve"),
    path('student/update/<pk>/',views.StudentUpdate.as_view(),  name="studentUpdate"),
    path('student/destroy/<pk>/',views.StudentDestroy.as_view(),  name="studentDestroy"),
]



