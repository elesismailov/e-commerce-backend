from rest_framework import serializers

from api.models import Order

from api.serializers.customer import CustomerSerializer
from api.serializers.status_code import StatusCodeSerializer


class OrderSerializer(serializers.Serializer):
    
    id               = serializers.IntegerField(read_only=True)

    customer         = CustomerSerializer(write_only=True)

    customer_comment = serializers.CharField(max_length=500)

    created_at       = serializers.DateTimeField(read_only=True)
    last_modified    = serializers.DateTimeField(read_only=True)

    status_code      = StatusCodeSerializer()


    class Meta:
        model = Order
