from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CustomerSerializer


@api_view(['POST'])
def sign_up(request):
    
    # serializer = CustomerSerializer(data=request.data)

    # if serializer.is_valid():

    #     serializer.save()
    # 
    #     print(serializer.data)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # print("not valid")
    # print(serializer.data)
    
    return Response('hello world')
