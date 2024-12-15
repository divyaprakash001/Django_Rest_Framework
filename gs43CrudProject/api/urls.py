from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', views.UserModelViewset,basename='hello')

urlpatterns = [
    path("",include(router.urls))
]
