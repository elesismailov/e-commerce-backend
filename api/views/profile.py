from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Customer
from api.serializers import CustomerSerializer

class Profile(APIView):
    """
    Customer's information.
    """

    def get(self, request):

        customer = request.customer

        serializer = CustomerSerializer(customer)

        return Response({
            'customer': serializer.data
            })

    def put(self, request):

        customer = request.customer

        customer.email = request.data.get('email', customer.email)
        customer.phone = request.data.get('phone', customer.phone)
        customer.name = request.data.get('name', customer.name)

        customer.save()

        serializer = CustomerSerializer(customer)

        return Response({
            'api_key': customer.api_key,
            'customer': serializer.data,
            })

























