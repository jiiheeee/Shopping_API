from django.urls import path
from . import views
from .views import CartaddView, CartListView

urlpatterns = [
    path("add/", CartaddView.as_view()),
    path("list/<int:user_id>", CartListView.as_view())
]