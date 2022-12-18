
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from admin.models import Staff


class AdminAuthenticationMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response


    def __call__(self, request):

        print(request.path)
        print(request.path[0:7])

        if (request.path[0:7] == '/admin/'):

            try:

                headers = request.headers.get('Authorization')
                api_key = headers.split(' ')[1]

                staff = Staff.objects.get(api_key=api_key)

            except Exception:

                response = Response(status=status.HTTP_401_UNAUTHORIZED)

                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response
            
            # success
            request.staff = staff

        response = self.get_response(request)


        return response









