from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Order
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

        print('/api/orders/ POST')

        return Response("Your response")

















