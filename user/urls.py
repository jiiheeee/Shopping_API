from django.urls import path
from .views import UserView

from . import views

urlpatterns = [
    path("<int:user_id>", views.index, name="index"),
    path("<str:user_name>", views.UserView.as_view()),
]