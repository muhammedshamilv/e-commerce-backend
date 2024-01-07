from django.shortcuts import render
from rest_framework.views import APIView
from products.models import *
from products.serializers.product_serializers import CartSerializer, OrderSerializer, ProductSerializer, CategorySerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.


class ProductPost(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            serialized_product = ProductSerializer(product).data
            return Response({"message": "Product created successfully", "product": serialized_product}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


# edit product
class UpdateProduct(APIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        try:
            instance = Product.objects.get(id=kwargs.get('id'))
        except Product.DoesNotExist:
            return Response({"message": "product not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = ProductSerializer(
                instance).data
            return Response({"message": "product updated successfully.", "data": serializer}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class GetCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# add to cart

# remove from cart


class GetCartItems(generics.ListAPIView,):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            instance = Cart.objects.filter(user=kwargs.get('user_id'))
        except Cart.DoesNotExist:
            return Response({"message": "cart items not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CartSerializer(
            instance, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)


#

class PostOrders(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

# get order by id

# delete order check time


class GetOrderedItems(generics.ListAPIView,):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            instance = Order.objects.filter(user=kwargs.get('user_id'))
        except Cart.DoesNotExist:
            return Response({"message": "order items not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(
            instance, many=True).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
