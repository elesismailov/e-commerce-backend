
from rest_framework import serializers

from api.models import Customer

class CustomerSerializer(serializers.Serializer):

    id               = serializers.IntegerField(read_only=True)

    name       = serializers.CharField(max_length=50, required=True)
    email      = serializers.EmailField(max_length=50, required=True)
    phone      = serializers.CharField(max_length=50, required=True)

    password   = serializers.CharField(max_length=50, write_only=True, required=True)

    created_at = serializers.DateTimeField(read_only=True)

    # api_key  = serializers.CharField(max_length=100)

    class Meta:
        model = Customer

    def create(self, validated_data):
        '''This is the serializer.save() method implementation.'''

        return Customer.objects.create(**validated_data)

