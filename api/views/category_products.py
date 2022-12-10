from api.models import Product, Category
from api.serializers import ProductSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class CategoryProducts(APIView):
    """
    List products of a category.
    """
    def get(self, request, slug):

        #TODO error handling

        try:
            category = Category.objects.get(slug=slug)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        products = Product.objects.filter(category=category).order_by('created_at')

        pagination = CustomPageNumberPagination()

        page = pagination.paginate_queryset(products, request)

        serializer = ProductSerializer(page, many=True)

        return pagination.get_paginated_response(serializer.data)










