from django.http import HttpResponse
from product.models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response

class ProductDetailView(APIView):
    def get(self, request, product_id:int):
        product_detail = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product_detail)
        return Response(serializer.data)

# 여러 개 filter, 한 개 가져올때는 get

class ProductSearchView(APIView):
    def get(self, request, product_name: str):
        product_list = Product.objects.filter(name__icontains=product_name) 
        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data)
