from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Product
from admin.serializers import ProductSerializer

class ProductView(APIView):
    '''
    /admin/products/<product_slug>/
    '''
    def get(self, request, slug):
        
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)

        return Response({
            'product': serializer.data
            })
