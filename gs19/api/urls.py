from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi',views.StudentReadOnlyModelViewSet, basename='student')

urlpatterns = [
    path("",include(router.urls))
]



