from unittest import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory

from unittest.mock import MagicMock, Mock, patch
from products.models import Category
from products.views import GetCategories

class GetCategoriesAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = GetCategories.as_view()

    @patch("products.views.GetCategories") 
    def test_get_category_unautherized(self,mock_user):
        request = self.factory.get("/product/category/")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)