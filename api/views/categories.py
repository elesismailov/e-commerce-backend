from api.models import Category
from api.serializers import CategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CategoryList(APIView):
    """
    List all Products, or create a new Product.
    """
    def get(self, request):

        #TODO error handling

        categories = Category.objects.all()

        serializer = CategorySerializer(page, many=True)

        return Response(serializer.data)
