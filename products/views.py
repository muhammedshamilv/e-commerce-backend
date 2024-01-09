from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.utils import timezone
from django.shortcuts import render
from rest_framework.views import APIView
from products.models import *
from products.serializers.product_serializers import CartSerializer, OrderSerializer, ProductSerializer, CategorySerializer
from datetime import datetime, timedelta
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

class GetAllProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
        'category__name': ['exact'],
        'price': ['gte', 'lte'],
    }
    search_fields = ['name', 'details', 'category__name']
    pagination_class = PageNumberPagination

class ProductDetailsAPI(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'PUT':
            return [IsAdminUser()]
        return super().get_permissions()




class GetCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class AddToCart(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class DeleteFromCart(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        try:
            instance = Cart.objects.get(id=kwargs.get('id'))
        except Cart.DoesNotExist:
            return Response({"message": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({"message": "Cart deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


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


class PostOrders(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class GetOrderDetails(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class DeleteOrder(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        try:
            instance = Order.objects.get(id=kwargs.get('id'))
        except Cart.DoesNotExist:
            return Response({"message": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
        current_datetime = timezone.now()
        if current_datetime - instance.created_at > timedelta(hours=12):
            return Response({"message": "Orders older than 12 hours cannot be deleted."}, status=status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response({"message": "Order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


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
