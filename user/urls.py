from django.urls import path
from .views import UserDetailView

from . import views

# TODO: 내정보 수정, 회원탈퇴, 블랙리스트, VIP리스트
urlpatterns = [
    path("<int:user_id>", UserDetailView.as_view())
]