from rest_framework import serializers
from products.models import *


class ProductSerializer(serializers.ModelSerializer):
    image=serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"
        read_only_field=("name","price","details","availability","image","category")
    def get_image(self,instance):
        if instance.image:
            return "http://127.0.0.1:8000"+instance.image.url 
        return "    " 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    # user=serializers.UUIDField()
    # product=serializers.UUIDField()
    
    class Meta:
        model = Cart
        fields = "__all__"

    def to_representation(self, instance):
        rep= super().to_representation(instance)
        rep["product"]=ProductSerializer(instance.product).data
        return rep
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        rep= super().to_representation(instance)
        rep["product"]=ProductSerializer(instance.product).data
        return rep
