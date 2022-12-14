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
    
    is_active       = serializers.BooleanField(read_only=True)

    price           = serializers.IntegerField()

    created_at      = serializers.DateTimeField(read_only=True)
    last_modified   = serializers.DateTimeField(read_only=True)

    brand           = BrandSerializer()
    category        = CategorySerializer()


    class Meta:
        model = Product

    def update(self, instance, data):

        instance.name            = data.get("name", instance.name) 
        instance.description     = data.get("description", instance.description) 

        instance.brand           = data.get('category', instance.brand)
        instance.category        = data.get('brand', instance.category)

        instance.slug            = data.get("slug", instance.slug) 
        instance.in_stock_amount = data.get("in_stock_amount", instance.in_stock_amount) 
        
        instance.sold_amount     = data.get("sold_amount", instance.sold_amount) 
        instance.is_active       = data.get("is_active", instance.is_active) 
        instance.price           = data.get("price", instance.price) 

        #instance.save()

        return instance
                 
                 
                 
                 
                 
                 
