from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import JSONParser

import json

from api.models import Order, OrderItem, CartItem, StatusCode
from api.serializers import OrderSerializer

class OrdersView(APIView):
    """
    List all customer orders.
    """

    def get(self, request):

        orders = Order.objects.filter(customer=request.customer).order_by('created_at')

        serializer = OrderSerializer(orders, many=True)

        return Response(
                {
                    "orders": serializer.data
                    }
                )

    def post(self, request):

        cart_items_data = request.data.get('cart_items')
        # address_to
        cart_items = []

        if not cart_items_data:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        order = Order.objects.create(
                customer         = request.customer,
                # customer_comment = customer_comment,
                status_code      = StatusCode.objects.first(),
                )


        # TODO check if given cart_item_it is active
        # getting all cart_items objects
        for data in cart_items_data:
            try:
                cart_item = CartItem.objects.get(id=int(data['cart_item_id']), is_active=True)

            except CartItem.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            cart_items.append(cart_item)

        # creating order_items (two loops are more readable)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                    order    = order,
                    product  = cart_item.product,
                    price    = cart_item.product.price,
                    quantity = cart_item.quantity,
                    )

            cart_item.is_active = False

        return Response("Your response")

















