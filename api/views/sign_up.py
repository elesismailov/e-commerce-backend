from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CustomerSerializer
from django.db.utils import IntegrityError


@api_view(['POST'])
def sign_up(request):
    
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()

        # already exists error
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT)

        # success
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # failed
    return Response(status=status.HTTP_400_BAD_REQUEST)
    # return Response("Please check whether you filled out all the fields.", status=status.HTTP_400_BAD_REQUEST)
