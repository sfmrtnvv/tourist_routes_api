from rest_framework import viewsets

from .models import (
    City,
    Route,
    Review
)

from .serializers import (
    CitySerializer,
    RouteSerializer,
    ReviewSerializer
)


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_queryset(self):
        queryset = City.objects.all()

        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(
                name__icontains=name
            )

        return queryset


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

    def get_queryset(self):
        queryset = Route.objects.all()

        city = self.request.query_params.get('city')

        max_price = self.request.query_params.get('max_price')

        if city:
            queryset = queryset.filter(
                city__name__icontains=city
            )

        if max_price:
            queryset = queryset.filter(
                price__lte=max_price
            )

        return queryset


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        queryset = Review.objects.all()

        route_id = self.request.query_params.get('route_id')

        if route_id:
            queryset = queryset.filter(
                route_id=route_id
            )

        return queryset