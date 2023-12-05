from django.db import models

class User(models.Model):
    realname = models.CharField(max_length = 200)
    phone = models.CharField(max_length =200)
    mail = models.CharField(max_length =200)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
