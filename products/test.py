from django.test import TestCase
from .models import Brand, Category, Product

class ProductModelTest(TestCase):
    def setUp(self):
       
        self.brand = Brand.objects.create(name="Nike")
        self.category = Category.objects.create(name="Sneakers")
        self.product = Product.objects.create(
            name="Air Max",
            brand=self.brand,
            category=self.category,
            price=120.00,
            stock=10,
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Air Max")
        self.assertEqual(self.product.price, 120.00)
        self.assertEqual(self.product.stock, 10)

    def test_product_str_method(self):
        self.assertEqual(str(self.product), "Air Max")
