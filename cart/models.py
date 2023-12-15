from django.db import models

class Cart(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, db_column="user_id")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, db_column="product_id")
    product_quantity = models.IntegerField()