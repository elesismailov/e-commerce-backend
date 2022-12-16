from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.pagination import PageNumberPagination

from api.models import Category
from admin.serializers import CategorySerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class CategoriesView(APIView):
    '''
    /admin/categories/
    '''
    def get(self, request):

        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)

        return Response({
            'categories': serializer.data
            })

















