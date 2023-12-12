# 데이터를 펼쳐준다 (직렬화)

from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    reservation_number = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    product = serializers.SerializerMethodField
    user = serializers.SerializerMethodField

class ReservationlistSerializer(serializers.ModelSerializer):

    reservation_number = serializers.CharField(required=True)
    user = serializers.SerializerMethodField
    product = serializers.SerializerMethodField
    created_at = serializers.DateTimeField(required=True)

    class Meta:
        model = Reservation
        fields = (
            'reservation_number',
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
