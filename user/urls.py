from django.urls import path
from .views import UserView

from . import views

# TODO: 내정보 수정, 회원탈퇴, 블랙리스트, VIP리스트
urlpatterns = [
    path("<int:user_id>", views.index, name="index"),
    path("<str:user_name>", views.UserView.as_view())
]