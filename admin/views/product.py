from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Product, Brand, Category
from admin.serializers import ProductSerializer

class ProductView(APIView):
    '''
    /admin/products/<product_slug>/
    '''
    def get(self, request, slug):
        
        try:
            product = Product.objects.get(slug=slug)#, is_active=True)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)

        return Response({
            'product': serializer.data
            })


    def put(self, request, slug):

        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        category_id     = data.get('category_id')
        brand_id        = data.get('brand_id')

        # finding category
        if (category_id != None) and isinstance(category_id, int): # ids are not integers
            try:
                category = Category.objects.get(id=category_id)
                instance.category = category

            except Category.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        # finding brand
        if (brand_id != None) and isinstance(brand_id, int): # ids are not integers
            try:
                brand    = Brand.objects.get(id=brand_id)
                instance.brand = brand

            except Brand.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        instance.name            = data.get("name", instance.name) 
        instance.description     = data.get("description", instance.description) 

        instance.slug            = data.get("slug", instance.slug) 
        instance.in_stock_amount = data.get("in_stock_amount", instance.in_stock_amount) 
        
        instance.sold_amount     = data.get("sold_amount", instance.sold_amount) 
        instance.is_active       = data.get("is_active", instance.is_active) 
        instance.price           = data.get("price", instance.price) 

        instance.save()

        serializer = ProductSerializer(instance)

        return Response({
            'product': serializer.data
            })


    def delete(self, request, slug):

        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            product.is_active = False
            product.save()

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = ProductSerializer(product)

        return Response({
            'product': serializer.data
            })

        



