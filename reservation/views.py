from rest_framework.response import Response
from rest_framework.views import APIView
from reservation.models import Reservation
from .serializers import ReservationSerializer

class ReservationView(APIView):
    def get(self, request, reservation_id:int):
        reservation_data = Reservation.objects.get(id=reservation_id)
        serializer = ReservationSerializer(reservation_data)
        return Response(serializer.data)

class RerservationlistView(APIView):
    def get(self, request, reservation_name):
        reservation_list = Reservation.objects.get(name=reservation_name)
        serializer = ReservationSerializer(reservation_list)
        return Response(serializer.data)


# def reservation_now(request, reservation_id:int):
#     reservation_data = Reservation.objects.get(id=reservation_id)
#     serializer = ReservationSerializer(reservation_data)
#     return Response(serializer.data)