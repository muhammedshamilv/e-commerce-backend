from django.views import View
from django.http import JsonResponse
from dj_rest_auth.registration.views import RegisterView
from user.serializers.user_serializer import CustomLoginSerializer, CustomRegisterSerializer
from dj_rest_auth.views import LoginView
from rest_framework import status


# Create your views here.


class HealthCheck(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"Health": "ok"})


class Account(RegisterView):
    serializer_class = CustomRegisterSerializer


class UserLogin(LoginView):
    serializer_class = CustomLoginSerializer

    def get_response(self):
        response = super().get_response()
        # Modify the response to include user ID
        if response.status_code == status.HTTP_200_OK:
            user = self.request.user
            print("response.data", response.data)
            response.data.pop('password', None)
            if user:
                response.data['user_id'] = user.id
                response.data['is_admin'] = user.is_superuser

        return response
