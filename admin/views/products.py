from api.models import Product
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.pagination import PageNumberPagination

from admin.serializers import ProductSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class ProductsView(APIView):
    '''
    /admin/products/
    '''
    def get(self, request):

        products = Product.objects.all().order_by('created_at')

        pagination = CustomPageNumberPagination()

        page = pagination.paginate_queryset(products, request)

        serializer = ProductSerializer(page, many=True)

        return pagination.get_paginated_response(serializer.data)

