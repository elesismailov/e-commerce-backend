
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import CartItem, Product
from api.serializers import CartItemSerializer

class CartView(APIView):
    """
    List all Cart Items.
    """
    def get(self, request):

        items = CartItem.objects.filter(
                customer=request.customer,
                is_active=True
               ).order_by('created_at')

        serializer = CartItemSerializer(items, many=True)

        return Response(
                {
                    'cart_items': serializer.data,
                    },
                )

    def post(self, request):

        quantity = request.data.get('quantity')
        product_id = request.data.get('product_id')

        if not quantity or not product_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            item = CartItem.objects.create(
                        customer=request.customer,
                        product=product,
                        quantity=quantity,
                    )

            serializer = CartItemSerializer(item)

            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                    )

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        










