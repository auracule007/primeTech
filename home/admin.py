from django.contrib import admin
from django.contrib.admin import ModelAdmin 
from . models import  *


# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'lat_long', 'full_details']
admin.site.register(Food, FoodAdmin)

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
admin.site.register(FoodItem, FoodItemAdmin)
