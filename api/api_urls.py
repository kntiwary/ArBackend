from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuildingViewSet, FloorViewSet, RoomViewSet, MarkerViewSet

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'floors', FloorViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'markers', MarkerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
