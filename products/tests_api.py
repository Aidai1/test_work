from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product, Brand, Category

class ProductAPITestCase(APITestCase):
    def setUp(self):
        # Dummy
        self.brand = Brand.objects.create(name="Adidas")
        self.category = Category.objects.create(name="Running Shoes")
        self.product = Product.objects.create(
            name="Ultraboost",
            brand=self.brand,
            category=self.category,
            price=150.00,
            stock=5,
        )

    def test_get_products_list(self):
        url = reverse('product-list')  # `urls.py`'да продукт лист API'нин атын текшерyy
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_product_detail(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Ultraboost")
