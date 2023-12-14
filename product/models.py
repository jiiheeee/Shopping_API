from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    distributor = models.CharField(max_length=200)
    sales_stock = models.IntegerField()
    remain_stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class CartAdd(models.Model):
    user = models.CharField(max_length=200)
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()

# Create your models here.
