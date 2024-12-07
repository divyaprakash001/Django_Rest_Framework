from django.urls import path,include

# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('studentApi/',views.StudentAPIView.as_view(), name="StudentAPIView"),
    # path('studentApi/',views.createStudent, name="studentApi"),
    path('studentApi/<id>',views.StudentAPIView.as_view(),  name="studentApi"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)