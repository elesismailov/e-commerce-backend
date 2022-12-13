
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Order, OrderItem, CartItem, StatusCode, Shipment
from api.serializers import OrderSerializer, OrderItemSerializer, ShipmentSerializer

class OrderView(APIView):
    """
    View details of an order.
    """

    def get(self, request, order_id):

        try:
            order = Order.objects.get(customer=request.customer, id=order_id)

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            order_items = OrderItem.objects.filter(order=order)

            orderSerializer = OrderSerializer(order)
            orderItemSerializer = OrderItemSerializer(order_items, many=True)

            return Response({
                        'order': orderSerializer.data,
                        'order_items': orderItemSerializer.data,
                    })

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OrderShipmentView(APIView):
    '''
    This view handles POST requests to create shipments for orders.
    '''

    def post(self, request, order_id):

        shipment_data = request.data.get('shipment')
        address_to    = shipment_data.get('address_to')

        if not shipment_data or not address_to:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.get(customer=request.customer, id=order_id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        shipment = Shipment.objects.create(
                order           = order,
                tracking_number = order.id, # TODO figure out what needs to go here
                address_to      = address_to,
                address_from    = 'Head Quarters', # TODO figure out what needs to go here
                )


        serializer = ShipmentSerializer(shipment)


        return Response({
            'shipment': serializer.data
            })













