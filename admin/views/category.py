
from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Category
from admin.serializers import CategorySerializer


class CategoryView(APIView):

    '''
    /admin/categories/<category-slug>/
    '''

    def get(self, request, slug):
        
        try:
            category = Category.objects.get(slug=slug)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)

        return Response({
            'category': serializer.data
            })











