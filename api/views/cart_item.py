from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import CartItem, Product
from api.serializers import CartItemSerializer

class CartItemView(APIView):
    """
    Updating cart items.
    """

    def put(self, request, cart_item_id):
        # TODO proper way would be to check whether there is the amount in stock
        try:
            cart_item = CartItem.objects.get(customer=request.customer, id=cart_item_id)

        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        quantity = request.data.get('quantity')

        
        if not quantity or not isinstance(quantity, int):
            return Response(status=status.HTTP_400_BAD_REQUEST)


        try:
            cart_item.quantity = quantity
            cart_item.save()
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = CartItemSerializer(cart_item)

        return Response({
            'cart_item': serializer.data
            })


    def delete(self, request, cart_item_id):

        # TODO proper way would be to check whether there is the amount in stock
        try:
            cart_item = CartItem.objects.get(customer=request.customer, id=cart_item_id)

        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        try:
            cart_item.delete()
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response()












