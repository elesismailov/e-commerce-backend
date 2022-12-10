from api.models import Category
from api.serializers import CategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class CategoryList(APIView):
    """
    List all Products, or create a new Product.
    """
    def get(self, request):

        categories = Category.objects.all()

        pagination = CustomPageNumberPagination()

        page = pagination.paginate_queryset(categories, request)

        serializer = CategorySerializer(page, many=True)

        return pagination.get_paginated_response(serializer.data)
