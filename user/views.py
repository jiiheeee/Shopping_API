from django.http import HttpResponse
from user.models import User

# [user.name이 안보임]
# def index(request, user_id:int):
#     from reservation.models import Reservation
#     reservation_list = Reservation.objects.select_related("user").filter(user_id=user_id)
#     result =[]
#     for reservation in reservation_list:
#         result.append(f"{reservation.user}가 {reservation.product}를 싰습니다.")
#     return HttpResponse(str(result))

# [실행이 안됨]
# def index(request, user_id:int):
#     from reservation.models import Reservation
#     reservation_list = User.objects.select_related("user").filter(user_id=user_id)
#     result =[]
#     for reservation in reservation_list:
#         result.append(f"{reservation.realname}가 {reservation.product}를 싰습니다.")
    # return HttpResponse(str(result))

def index(request, user_id:int):
    from reservation.models import Reservation
    reservation_list = Reservation.objects.select_related("user").filter(user_id=user_id)
    result =[]
    for reservation in reservation_list:
        result.append(f"{reservation.user.realname}가 {reservation.product.name}를 싰습니다.")
    return HttpResponse(str(result))
    
