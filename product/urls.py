from django.urls import path
from . import views
from .views import ProductSearchView

# TODO : 상품상세
urlpatterns = [
    path("<int:product_id>", views.get_remain_stock, name="get_remain_stock"),
    path("search/<str:product_name>", ProductSearchView.as_view())
]