from django.http import HttpResponse
from product.models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response

def get_remain_stock(request, product_id:int):
    product = Product.objects.get(id=product_id)
    return HttpResponse(f"{product.name}의 남은 수량은 {product.remain_stock}입니다.")

# 여러 개 filter, 한 개 가져올때는 get

class ProductSearchView(APIView):
    def get(self, request, product_name: str):
        product_list = Product.objects.filter(name=product_name)
        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data)
        