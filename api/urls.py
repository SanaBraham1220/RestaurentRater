from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import RestaurentViewSet,RatingViewSet

router = routers.DefaultRouter()
router.register('restaurent',RestaurentViewSet)
router.register('rating',RatingViewSet)
urlpatterns = [
    path('',include(router.urls))
]

