
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Cart, CartItem
from api.serializers import CartItemSerializer

class CartView(APIView):
    """
    List all Cart Items.
    """
    def get(self, request):

        try:
            cart = Cart.objects.get(customer=request.customer)
        except Cart.DoesNotExist:
            Cart.objects.create(customer=request.customer)

            return Response({'cart_items': []})


        items = CartItem.objects.filter(cart=cart).order_by('created_at')

        serializer = CartItemSerializer(items, many=True)

        return Response(
                {
                    'cart_items': serializer.data,
                    },
                )





