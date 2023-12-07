from django.http import HttpResponse
from user.models import User
from rest_framework.views import APIView
from user.models import User


class SignUpView(APIView):
    def post(self, request):
        """
            post 요청에서 데이터를 가져올때 -> request.data.get("컬럼명")
            get 요청에서 데이터를 가져올때 -> request.query_params.get("컬럼명")
        """
        name = request.data.get("name")
        password = request.data.get('password')
        phone = request.data.get('phone')
        mail = request.data.get('mail')
        """
            1. 객체를 만든다음에 save하는 방식
                user = User(name=name, password=password, phone=phone, mail=mail)
                user.save()
            2. 클래스의 ORM을 사용하는 방식
                new_user = User.objects.create(name, password, phone, mail)
        """
        User.objects.create(
            realname=name, 
            password=password, 
            phone=phone, 
            mail=mail, 
            is_active=True
        )
        return HttpResponse('회원가입이 완료되었습니다.')
