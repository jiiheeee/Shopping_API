from django.urls import path
from .views import UserDetailView

from . import views

urlpatterns = [
    path("<int:user_id>", UserDetailView.as_view())
]