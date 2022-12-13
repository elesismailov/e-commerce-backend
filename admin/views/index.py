from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):
    '''
    /admin/
    '''
    def get(self, request):

        return Response('This is the admin index page.')
