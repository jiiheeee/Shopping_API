from django.http import HttpResponse
from rest_framework.response import Response
from user.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer

def index(request, user_id:int):
    from reservation.models import Reservation
    reservation_list = Reservation.objects.select_related("user").filter(user_id=user_id)
    result =[]
    for reservation in reservation_list:
        result.append(f"{reservation.user.realname}가 {reservation.product.name}를 싰습니다.")
    return HttpResponse(str(result))
    
class UserView(APIView):
    def get(self, request, user_name:str):
        user_detail = User.objects.get(realname=user_name)
        serializer = UserSerializer(user_detail)
        return Response(serializer.data)