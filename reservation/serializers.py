# 데이터를 펼쳐준다 (직렬화)

from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    product = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Reservation
        fields = (
            'name',
            'created_at',
            'product',
            'user'
        )
    @staticmethod
    def get_product(obj):
        return obj.product.name
    
    @staticmethod
    def get_user(obj):
        return obj.user.realname
    