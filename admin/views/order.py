from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from admin.serializers import OrderSerializer
from api.serializers import OrderItemSerializer
from api.models import Order, OrderItem, StatusCode, Category, Product


class OrderView(APIView):

    '''
    /admin/orders/<order-id>/
    '''

    def get(self, request, order_id):

        try:
            order = Order.objects.get(id=order_id)

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        order_items = OrderItem.objects.filter(order=order)

        order_serializer = OrderSerializer(order)
        order_items_serializer = OrderItemSerializer(order_items, many=True)

        return Response({
            'order': order_serializer.data,
            'order_items': order_items_serializer.data,
            })


    def put(self, request, order_id):

        try:
            order = Order.objects.get(id=order_id)

        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        status_code_id = request.data.get('status_code_id')

        try:
            status_code = StatusCode.objects.get(id=status_code_id)

        except StatusCode.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        order.status_code = status_code

        order.save()

        serializer = OrderSerializer(order)

        return Response({
            'order': serializer.data
            })



























        
