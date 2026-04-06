import unittest
import sys
import os

# Добавляем путь к src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.Product import Product


class TestProduct(unittest.TestCase):
    """Тесты для класса Product"""

    def setUp(self):
        """Подготовка данных для тестов"""
        self.product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    def test_product_initialization(self):
        """Тест корректной инициализации объекта Product"""
        self.assertEqual(self.product1.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(self.product1.description, "256GB, Серый цвет, 200MP камера")
        self.assertEqual(self.product1.price, 180000.0)
        self.assertEqual(self.product1.quantity, 5)

    def test_product_different_attributes(self):
        """Тест инициализации разных продуктов"""
        self.assertEqual(self.product2.name, "Iphone 15")
        self.assertEqual(self.product2.price, 210000.0)
        self.assertEqual(self.product2.quantity, 8)

        self.assertEqual(self.product3.name, "Xiaomi Redmi Note 11")
        self.assertEqual(self.product3.price, 31000.0)
        self.assertEqual(self.product3.quantity, 14)

    def test_product_price_type(self):
        """Тест типа данных цены"""
        self.assertIsInstance(self.product1.price, float)
        self.assertIsInstance(self.product2.price, float)

    def test_product_quantity_type(self):
        """Тест типа данных количества"""
        self.assertIsInstance(self.product1.quantity, int)
        self.assertIsInstance(self.product2.quantity, int)

    def test_product_name_type(self):
        """Тест типа данных названия"""
        self.assertIsInstance(self.product1.name, str)
        self.assertIsInstance(self.product2.name, str)

    def test_product_with_zero_quantity(self):
        """Тест продукта с нулевым количеством"""
        product = Product("Test", "Test description", 100.0, 0)
        self.assertEqual(product.quantity, 0)

    def test_product_with_float_price(self):
        """Тест продукта с ценой в виде числа с плавающей точкой"""
        product = Product("Test", "Test description", 99.99, 10)
        self.assertEqual(product.price, 99.99)
        self.assertIsInstance(product.price, float)
