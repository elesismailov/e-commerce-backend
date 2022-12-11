from rest_framework import serializers

from api.models import CartItem
from api.serializers import ProductSerializer


class CartItemSerializer(serializers.Serializer):
    
    # cart             = serializers.EmptyFieldLOL()
    product          = ProductSerializer()

    quantity         = serializers.IntegerField()

    # price_expires_at = serializers.DateTimeField()

    created_at       = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CartItem
        fields = ['name', 'description']
