from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import StatusCodeSerializer
from api.models import StatusCode


class StatusCodesView(APIView):


    def get(self, request):

        status_codes = StatusCode.objects.all()

        serializer = StatusCodeSerializer(status_codes, many=True)

        return Response({
            'status_codes': serializer.data
            })
































