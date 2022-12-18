from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import StatusCodeSerializer
from api.models import StatusCode


class StatusCodeView(APIView):
    '''
    /admin/status_codes/<status_code_id>/
    '''

    def get(self, request, status_code_id):

        try:
            status_code = StatusCode.objects.get(id=status_code_id)

        except StatusCode.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StatusCodeSerializer(status_code)

        return Response({
            'status_code': serializer.data
            })


    def put(self, request, status_code_id):

        try:
            status_code = StatusCode.objects.get(id=status_code_id)

        except StatusCode.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        status_code.code        = request.data.get('code', status_code.code)
        status_code.name        = request.data.get('name', status_code.name)
        status_code.description = request.data.get('description', status_code.description)

        status_code.save()

        serializer = StatusCodeSerializer(status_code)
        
        return Response({
            'status_code': serializer.data,
            })





































