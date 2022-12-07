from rest_framework import serializers

from api.models import Category

class CategorySerializer(serializers.Serializer):

    name            = serializers.CharField(max_length=50)
    description     = serializers.CharField(max_length=250)
    
    slug            = serializers.CharField(max_length=50)

    class Meta:
        model = Category
        fields = ['name', 'description']