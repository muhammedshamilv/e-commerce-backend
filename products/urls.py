from django.urls import path

from products.views import GetAllProducts, GetCategories, GetCartItems

urlpatterns = [
    path("", GetAllProducts.as_view(), name="products"),
    path("category/", GetCategories.as_view(), name="categories"),
    path("user/<uuid:user_id>/cart/", GetCartItems.as_view(), name="cart-items"),


]
