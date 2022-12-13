from rest_framework import serializers

from api.models import CartItem
from api.serializers import ProductSerializer
from api.serializers.customer import CustomerSerializer


class CartItemSerializer(serializers.Serializer):
    
    id               = serializers.IntegerField(read_only=True)

    customer         = CustomerSerializer(write_only=True)

    quantity         = serializers.IntegerField()

    is_active        = serializers.BooleanField()

    checked_out_at   = serializers.DateTimeField()

    last_modified    = serializers.DateTimeField(read_only=True)
    created_at       = serializers.DateTimeField(read_only=True)

    product          = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['name', 'description']







