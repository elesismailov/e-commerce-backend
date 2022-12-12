from rest_framework import serializers

from api.models import Shipment

from api.serializers.order import OrderSerializer


class ShipmentSerializer(serializers.Serializer):
    
    id               = serializers.IntegerField(read_only=True)

    order            = OrderSerializer(write_only=True)

    tracking_number  = serializers.IntegerField()

    address_to       = serializers.CharField(max_length=100)
    address_from     = serializers.CharField(max_length=100)

    created_at       = serializers.DateTimeField(read_only=True)
    last_modified    = serializers.DateTimeField(read_only=True)


    class Meta:
        model = Shipment
