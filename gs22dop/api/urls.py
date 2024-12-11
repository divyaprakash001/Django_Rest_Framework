from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()

router.register('studentapi', StudentViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls'))
]
