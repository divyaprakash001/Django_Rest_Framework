from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentlist',views.StudentModelViewSet, basename='student')

urlpatterns = [
    path("",include(router.urls)),
]
