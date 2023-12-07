from django.urls import path
from .views import ReservationView
from .views import RerservationlistView

from . import views

urlpatterns = [
    path("<int:reservation_id>", ReservationView.as_view()),
    path("<int:reservation_name>", ReservationlistView.as_view())
]