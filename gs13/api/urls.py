from django.urls import path
from . import views

urlpatterns = [
    # path('studentApi/',views.createStudent, name="studentApi"),
    path('studentLCApi/',views.StudentListCreate.as_view(),  name="studentLCApi"),
    path('studentRUDApi/<pk>/',views.StudentRUDList.as_view(),  name="studentRUDApi"),
]



