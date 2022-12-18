from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import IntegrityError

from api.serializers import StatusCodeSerializer
from api.models import StatusCode


class StatusCodesView(APIView):


    def get(self, request):

        status_codes = StatusCode.objects.all()

        serializer = StatusCodeSerializer(status_codes, many=True)

        return Response({
            'status_codes': serializer.data
            })

    
    def post(self, request):

        code        = request.data.get('code')
        name        = request.data.get('name')
        description = request.data.get('description')

        if (
                not code or
                not name or
                not description
            ):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            status_code = StatusCode.objects.create(
                    code = code,
                    name = name,
                    description = description,
                    )
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            raise e


        serializer = StatusCodeSerializer(status_code)

        return Response({
            'status_code': serializer.data,
            })































