from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singer',views.SingerViewSet, basename='singer')
router.register('song',views.SongViewSet, basename='song')

urlpatterns = [
    path("", include(router.urls)),
]
