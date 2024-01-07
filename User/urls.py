from django.urls import path

from User.views import HealthCheck

urlpatterns = [
    path("", HealthCheck.as_view(), name="health"),


]
