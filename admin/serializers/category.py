from rest_framework import serializers

from api.models import Category

class CategorySerializer(serializers.Serializer):
    
    id                 = serializers.IntegerField(read_only=True)

    name               = serializers.CharField(max_length=50)
    description        = serializers.CharField(max_length=250)

    #parent_category   = CategorySerializer()

    is_active          = serializers.BooleanField()

    parent_category_id = serializers.SerializerMethodField()
    
    slug               = serializers.CharField(max_length=50)

    created_at         = serializers.DateTimeField(read_only=True)
    last_modified      = serializers.DateTimeField(read_only=True)


    def get_parent_category_id(self, instance):

        return instance.parent_category.id if instance.parent_category else None

    class Meta:
        model = Category
        fields = ['name', 'description']
