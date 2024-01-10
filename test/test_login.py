from unittest import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory


from user.models import User
from user.views import UserLogin


class UserLoginAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserLogin.as_view()

    def test_login_(self):
        data = {
            "email": "shamil@gmail.com",
            "password": "shamil",
        }
        request = self.factory.post("/sign-in/", data=data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)