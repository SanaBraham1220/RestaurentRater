from django.contrib import admin
from .models import Restaurent,Rating

class RestaurentAdmin(admin.ModelAdmin):
    list_display = ['title','adress','nbrstars']
    list_filter = ['nbrstars']
    
class RatingAdmin(admin.ModelAdmin):
    list_display = ['restaurent','user','rating']
    list_filter = ['restaurent','user','rating']

admin.site.register(Restaurent,RestaurentAdmin)
admin.site.register(Rating,RatingAdmin)