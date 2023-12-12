from django.urls import path
from .views import ReservationView, ReservationListView, ReservationAddView

from . import views

urlpatterns = [
    path("<int:user_id>/<int:reservation_id>", ReservationView.as_view()),
    path("<int:user_id>", ReservationListView.as_view()),
    path("orderadd/", ReservationAddView.as_view())
]