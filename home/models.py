from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    items = models.ManyToManyField('FoodItem')
    lat_long = models.CharField(max_length= 200, null=True, blank=True)
    full_details = models.TextField()

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
