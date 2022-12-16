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


    def post(self, request):

        data = request.data

        name = data.get('name')
        description = data.get('description')
        parent_category_id = data.get('parent_category_id')

        if not name:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            parent_category = Category.objects.get(id=parent_category_id)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        category = Category.objects.create(
                name = name,
                description = description,
                parent_category = parent_category,
                )

        serializer = CategorySerializer(category)

        return Response({
            'category': serializer.data
            })
 















