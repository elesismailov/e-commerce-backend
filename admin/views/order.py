from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from admin.serializers import CategorySerializer, ProductSerializer
from api.models import Order, StatusCode, Category, Product
from api.serializers import OrderSerializer

from rest_framework.pagination import PageNumberPagination

from admin.helpers.count_orders import count_orders




class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class OrderView(APIView):

    '''
    /admin/orders/<status-code-slug>
    '''

    def get(self, request, slug):

        
        try:
            status_code = StatusCode.objects.get(slug=slug)

        except StatusCode.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        orders = Order.objects.filter(status_code=status_code).order_by('last_modified')

        pagination = CustomPageNumberPagination()
        page = pagination.paginate_queryset(orders, request)
        serializer = OrderSerializer(page, many=True)

        count = count_orders()

        return pagination.get_paginated_response({
            'count': count,
            'orders': serializer.data,
            })









