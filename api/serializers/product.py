from rest_framework import serializers

from api.models import Product

# accessing file to avoid circular import 
from api.serializers.category import CategorySerializer
from api.serializers.brand import BrandSerializer


class ProductSerializer(serializers.Serializer):
    
    name            = serializers.CharField(max_length=50)
    description     = serializers.CharField(max_length=250)
    
    slug            = serializers.CharField(max_length=50)

    brand           = BrandSerializer()
    category        = CategorySerializer()

    in_stock_amount = serializers.IntegerField()
    sold_amount     = serializers.IntegerField()
    
    price           = serializers.IntegerField()

    created_at      = serializers.DateTimeField(read_only=True)
    last_modified   = serializers.DateTimeField()


    class Meta:
        model = Product
        fields = ['name', 'description']
