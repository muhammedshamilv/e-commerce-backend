from django.urls import path

from user.views import HealthCheck, Account, UserLogin

urlpatterns = [
    path("", HealthCheck.as_view(), name="health"),
    path("sign-up/", Account.as_view(), name="sign-up"),
    path("sign-in/", UserLogin.as_view(), name="sign-ip"),
]
