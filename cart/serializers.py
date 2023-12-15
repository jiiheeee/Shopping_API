from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField
    product = serializers.SerializerMethodField
    product_quantity = serializers.CharField(required=True)

    class Meta:
        model = Cart
        fields = (
            'user',
            'product',
            'product_quantity'
        )

    @staticmethod
    def get_product(obj):
        return obj.product.name

    @staticmethod
    def get_user(obj):
        return obj.user.realname