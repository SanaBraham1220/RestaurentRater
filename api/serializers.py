from rest_framework import serializers
from .models import Restaurent,Rating

class RestaurentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurent
        fields = ['id','title','description','adress','nbrstars']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','user','restaurent','rating')
    