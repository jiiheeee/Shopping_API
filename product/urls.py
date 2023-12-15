from django.urls import path
from . import views
from .views import ProductSearchView, ProductDetailView

urlpatterns = [
    path("<int:product_id>", ProductDetailView.as_view()),
    path("search/<str:product_name>", ProductSearchView.as_view())
]