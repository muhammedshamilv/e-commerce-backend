from django.shortcuts import render
from rest_framework.views import APIView
from products.models import *
from products.serializers.product_serializers import ProductSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.


class GetAllProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
