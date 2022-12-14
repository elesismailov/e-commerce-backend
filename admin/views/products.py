from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from psycopg2.errors import NotNullViolation

from rest_framework.pagination import PageNumberPagination

from api.models import Product, Brand, Category
from admin.serializers import ProductSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class ProductsView(APIView):
    '''
    /admin/products/
    '''
    def get(self, request):

        products = Product.objects.all().order_by('created_at')

        pagination = CustomPageNumberPagination()

        page = pagination.paginate_queryset(products, request)

        serializer = ProductSerializer(page, many=True)

        return pagination.get_paginated_response(serializer.data)



    def post(self, request):

        data = request.data

        name            = data.get('name')
        description     = data.get('description')
        category_id     = data.get('category_id')
        brand_id        = data.get('brand_id')
        in_stock_amount = data.get('in_stock_amount')
        sold_amount     = data.get('sold_amount', 0)
        price           = data.get('price')

        # validate submited data
        if (
                not name or not description or # name or desc are not given
                price == None or price < 1 or  # price isn't given or negative
                in_stock_amount == None or in_stock_amount < 1 or # in_stock_amount is not given or negative
                category_id == None or brand_id == None or # ids are not given
                not isinstance(category_id, int) or # ids are not integers
                not isinstance(brand_id, int)
            ):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # finding category and brand
        try:
            category = Category.objects.get(id=category_id)
            brand    = Brand.objects.get(id=brand_id)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try: 
            product = Product.objects.create(
                name            = name,
                description     = description,
                category        = category,
                brand           = brand,
                in_stock_amount = in_stock_amount,
                sold_amount     = sold_amount,
                price           = price,
                )

        except ValidationError or NotNullViolation:
            print(ValidationError)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise e
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = ProductSerializer(product)

        return Response({
            'product': serializer.data
            })

















