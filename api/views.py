from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurent,Rating
from .serializers import RestaurentSerializer,RatingSerializer

class RestaurentViewSet(viewsets.ModelViewSet):
    queryset = Restaurent.objects.all()
    serializer_class = RestaurentSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

