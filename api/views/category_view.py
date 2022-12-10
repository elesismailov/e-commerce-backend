from api.models import Category
from api.serializers import CategorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryView(APIView):

    def get(self, request, slug):

        try:
            category = Category.objects.get(slug=slug)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = CategorySerializer(category) 

        return Response(serializer.data)
