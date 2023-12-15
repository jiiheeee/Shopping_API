from django.urls import path
from . import views
from .views import CartaddView

urlpatterns = [
    path("add/", CartaddView.as_view())
]