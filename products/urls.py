from django.urls import path

from products.views import GetAllProducts

urlpatterns = [
    path("", GetAllProducts.as_view(), name="products"),
]
