from django.shortcuts import render
from rest_framework.views import APIView
from products.models import *
from products.serializers.product_serializers import CartSerializer, ProductSerializer, CategorySerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.


class GetAllProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class GetCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class GetCartItems(generics.ListAPIView,):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            instance = Cart.objects.get(user=kwargs.get('user_id'))
        except Cart.DoesNotExist:
            return Response({"message": "cart items not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CartSerializer(
            instance).data
        return Response({"data": serializer}, status=status.HTTP_200_OK)
