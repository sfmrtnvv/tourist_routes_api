from django.urls import (
    path,
    include
)

from rest_framework.routers import DefaultRouter

from .views import (
    CityViewSet,
    RouteViewSet,
    ReviewViewSet
)

router = DefaultRouter()

router.register(r'cities', CityViewSet)

router.register(r'routes', RouteViewSet)

router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]