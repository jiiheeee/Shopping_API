from django.urls import path
from .views import ReservationView, ReservationListView, ReservationAddView, ReservationCancel

from . import views

urlpatterns = [
    path("<int:user_id>/<int:reservation_id>", ReservationView.as_view()),
    path("<int:user_id>", ReservationListView.as_view()),
    path("orderadd/", ReservationAddView.as_view()),
    path("cancel/<int:reservation_id>", ReservationCancel.as_view())
]