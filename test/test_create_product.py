import pytest
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.urls import reverse
from products.models import Product
from products.serializers.product_serializers import ProductSerializer
from products.views import ProductPost


@pytest.mark.django_db(transaction=False)
def test_product_post_view_without_db():
    factory = APIRequestFactory()
    url = reverse('create-products')  # Replace with your actual URL name

    data = {
        'name': 'Test Product',
        'price': '10.99',
        'details': 'Test details',
        'availability': 5,
        # Add other required fields as needed
    }

    request = factory.post(url, data, format='json')
    view = ProductPost.as_view()
    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED
    # Add other assertions as needed
