from rest_framework import serializers

from api.models import OrderItem

from api.serializers.product import ProductSerializer


class OrderItemSerializer(serializers.Serializer):
    
    id            = serializers.IntegerField(read_only=True)

    price         = serializers.IntegerField()

    quantity      = serializers.IntegerField()

    created_at    = serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField(read_only=True)

    product       = ProductSerializer(read_only=True)


    class Meta:
        model = OrderItem
