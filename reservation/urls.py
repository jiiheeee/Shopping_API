from django.urls import path
from .views import ReservationView, ReservationlistView

from . import views

urlpatterns = [
    path("<int:reservation_id>", ReservationView.as_view()),
    path("<str:user_name>", ReservationlistView.as_view())
]