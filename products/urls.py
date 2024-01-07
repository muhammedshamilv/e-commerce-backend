from django.urls import path

from products.views import GetAllProducts, GetCategories, GetCartItems, GetOrderedItems, GetProductDetails

urlpatterns = [
    path("", GetAllProducts.as_view(), name="products"),
    path("category/", GetCategories.as_view(), name="categories"),
    path("user/<uuid:user_id>/cart/", GetCartItems.as_view(), name="cart-items"),
    path("user/<uuid:user_id>/orders/",
         GetOrderedItems.as_view(), name="order-items"),
    path("<uuid:id>/", GetProductDetails.as_view(), name="products-details"),


]
