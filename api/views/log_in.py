from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.utils import IntegrityError

from api.serializers import CustomerSerializer


@api_view(['POST'])
def log_in(request):
    
    return Response('Loggin in...')
