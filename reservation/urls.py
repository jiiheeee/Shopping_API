from django.urls import path
from .views import ReservationView

from . import views

urlpatterns = [
    path("<int:reservation_id>", ReservationView.as_view()),
]