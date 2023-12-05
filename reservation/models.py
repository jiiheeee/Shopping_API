from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, db_column="user_id")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, db_column="product_id")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
