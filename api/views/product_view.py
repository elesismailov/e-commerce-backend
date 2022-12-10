from api.models import Product
from api.serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductView(APIView):

    def get(self, request, slug):

        try:
            product = Product.objects.get(slug=slug)

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = ProductSerializer(product) 

        return Response(serializer.data)
