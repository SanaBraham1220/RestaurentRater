from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Restaurent(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    adress = models.CharField(max_length=50)
    nbrstars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],null=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    
    restaurent = models.ForeignKey(Restaurent,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','restaurent'),)
        index_together = (('user','restaurent'),)