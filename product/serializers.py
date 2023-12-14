from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    distributor = serializers.CharField(required=True)
    sales_stock = serializers.IntegerField(required=True)
    remain_stock = serializers.IntegerField(required=True)
    created_at = serializers.DateTimeField(required=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'distributor',
            'sales_stock',
            'remain_stock',
            'created_at'
        )

