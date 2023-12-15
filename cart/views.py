from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from cart.models import Cart
from .serializers import CartSerializer


class CartaddView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        product_id = request.data.get("product_id")
        product_quantity = request.data.get("product_quantity")
        
        # from user.models import User
        # user = User.objects.get(id=1)
        # Cart.objects.get(user=user_id)
        
        Cart.objects.create(
            user_id=user_id,
            product_id=product_id,
            product_quantity=product_quantity
        )
        return HttpResponse('장바구니에 담겼습니다.')
    
    # def get(self, request, user: int):
    #     item_cart = Cart.objects.filter(user__id=user)
    #     serializer = CartSerializer(item_cart, many=True)
    #     return Response(serializer.data)