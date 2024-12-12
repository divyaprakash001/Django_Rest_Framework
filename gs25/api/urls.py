from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('studentapi',views.StudentModelViewSet, basename='student')

urlpatterns = [
    path("",include(router.urls)),
    path("auth/", include('rest_framework.urls', namespace='rest_framework')),
    path("gettoken/", obtain_auth_token),
]



