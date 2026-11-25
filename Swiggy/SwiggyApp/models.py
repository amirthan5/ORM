from os import name

from django.db import models
from django.contrib import admin

class Swiggy(models.Model):
    order_id = models.CharField(max_length=7)
    customer_name = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=30)
    food_item = models.CharField(max_length=20)
    total_amount = models.FloatField()
    payment_method = models.CharField(max_length=20)
    order_status = models.CharField(max_length=30)
    delivery_time = models.IntegerField()

class SwiggyAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'restaurant_name', 'food_item', 'total_amount', 'payment_method', 'order_status', 'delivery_time')