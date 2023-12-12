from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from reservation.models import Reservation
from .serializers import ReservationSerializer

class ReservationView(APIView):
    def get(self, request, user_id: int, reservation_id: int):
        try:
            reservation_data = Reservation.objects.get(id=reservation_id, user__id=user_id)
        except Exception as e:
            return Response("해당 고객이 주문한 주문내역이 아닙니다.", status=400)
        serializer = ReservationSerializer(reservation_data)
        return Response(serializer.data, status=200)

class ReservationListView(APIView):
    def get(self, request, user_id: int):
        order_list = Reservation.objects.filter(user__id=user_id)
        serializer = ReservationSerializer(order_list, many=True)
        return Response(serializer.data)
    
class ReservationAddView(APIView):
    def post(self, request):
        reservation_number = request.data.get("reservation_number")
        user = request.data.get("user_id")
        product = request.data.get("product_id")

        Reservation.objects.create(
        reservation_number=reservation_number,
        user_id=user,
        product_id=product
        )
        return HttpResponse('주문이 완료되었습니다.')