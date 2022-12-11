from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from django.conf import settings
from django.urls import path

from api.models import Customer


class APIAuthenticationMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response


    def __call__(self, request):

        routes = settings.API_PROTECTED_ROUTES

        for route in routes:
            u = path(route, lambda x: print(x))

            if u.pattern.match(request.path):

                try:

                    headers = request.headers.get('Authorization')
                    api_key = headers.split(' ')[1]

                    customer = Customer.objects.get(api_key=api_key)

                # except Customer.DoesNotExist:
                except Exception:

                    response = Response(status=status.HTTP_401_UNAUTHORIZED)

                    response.accepted_renderer = JSONRenderer()
                    response.accepted_media_type = "application/json"
                    response.renderer_context = {}
                    response.render()
                    return response
                
                # success
                request.customer = customer

        response = self.get_response(request)


        return response











