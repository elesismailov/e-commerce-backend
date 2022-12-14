from rest_framework import serializers

from api.models import Product

# accessing file to avoid circular import 
from api.serializers.category import CategorySerializer
from api.serializers.brand import BrandSerializer


class ProductSerializer(serializers.Serializer):
    
    id              = serializers.IntegerField(read_only=True)
    
    name            = serializers.CharField(max_length=50)
    description     = serializers.CharField(max_length=250)
    
    slug            = serializers.CharField(max_length=50)

    in_stock_amount = serializers.IntegerField()
    sold_amount     = serializers.IntegerField()
    
    price           = serializers.IntegerField()

    created_at      = serializers.DateTimeField(read_only=True)
    last_modified   = serializers.DateTimeField(read_only=True)

    brand           = BrandSerializer()
    category        = CategorySerializer()


    class Meta:
        model = Product
