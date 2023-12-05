from django.urls import path

from . import views

urlpatterns = [
    path("<int:product_id>", views.get_remain_stock, name="get_remain_stock"),
]