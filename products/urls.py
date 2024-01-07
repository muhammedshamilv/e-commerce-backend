from django.urls import path

from products import views
urlpatterns = [
    path("", views.GetAllProducts.as_view(), name="products"),
    path("create/", views.ProductPost.as_view(), name="create-products"),
    path("<uuid:id>/", views.UpdateProduct.as_view(), name="update-products"),
    path("<uuid:id>/", views.GetProductDetails.as_view(), name="products-details"),

    path("category/", views.GetCategories.as_view(), name="categories"),

    path("user/<uuid:user_id>/cart/",
         views.GetCartItems.as_view(), name="cart-items"),
    path("cart/",
         views.AddToCart.as_view(), name="add-to-cart"),
    path("cart/remove/<uuid:id>/",
         views.DeleteFromCart.as_view(), name="remove-from-cart"),




    path("user/<uuid:user_id>/orders/",
         views.GetOrderedItems.as_view(), name="ordered-items"),
    path("order/",
         views.PostOrders.as_view(), name="order-items"),
    path("order/<uuid:id>/details/",
         views.GetOrderDetails.as_view(), name="order-details"),
    path("order/remove/<uuid:id>/",
         views.DeleteOrder.as_view(), name="delete-order"),


]
