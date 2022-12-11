
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import CartItem
from api.serializers import CartItemSerializer

class CartView(APIView):
    """
    List all Cart Items.
    """
    def get(self, request):

        items = CartItem.objects.filter(
                customer=request.customer,
                is_active=True
               ).order_by('created_at')

        serializer = CartItemSerializer(items, many=True)

        return Response(
                {
                    'cart_items': serializer.data,
                    },
                )





