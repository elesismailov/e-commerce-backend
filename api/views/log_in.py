from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import check_password

from api.serializers import CustomerSerializer
from api.models import Customer


@api_view(['POST'])
def log_in(request):

    try:
        customer = Customer.objects.get(email=request.data.get('email'))

        if check_password(
                request.data.get('password'), # string password
                customer.password, # hashed password
                ):

            serializer = CustomerSerializer(customer)

            return Response({
                'api_key': customer.api_key,
                'customer_data': serializer.data,
                })

    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
