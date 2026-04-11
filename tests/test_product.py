import unittest
from src.Product import Product


class TestProduct(unittest.TestCase):
    """Тесты для класса Product"""

    def setUp(self):
        self.product = Product("Телефон", "Смартфон", 50000.0, 10)

    def test_price_getter(self):
        """Тест геттера цены"""
        self.assertEqual(self.product.price, 50000.0)

    def test_price_setter_positive(self):
        """Тест сеттера с положительной ценой"""
        self.product.price = 60000.0
        self.assertEqual(self.product.price, 60000.0)

    def test_price_setter_zero(self):
        """Тест сеттера с нулевой ценой"""
        self.product.price = 0
        self.assertEqual(self.product.price, 50000.0)  # Цена не изменилась

    def test_price_setter_negative(self):
        """Тест сеттера с отрицательной ценой"""
        self.product.price = -100
        self.assertEqual(self.product.price, 50000.0)  # Цена не изменилась

    def test_new_product_class_method_with_dict(self):
        """Тест класс-метода new_product со словарём"""
        product_data = {
            "name": "Ноутбук",
            "description": "Игровой ноутбук",
            "price": 80000.0,
            "quantity": 5
        }
        product = Product.new_product(product_data)

        self.assertEqual(product.name, "Ноутбук")
        self.assertEqual(product.description, "Игровой ноутбук")
        self.assertEqual(product.price, 80000.0)
        self.assertEqual(product.quantity, 5)

    def test_new_product_missing_key(self):
        """Тест на отсутствие обязательного ключа в словаре"""
        incomplete_data = {
            "name": "Ноутбук",
            "price": 80000.0
            # отсутствуют 'description' и 'quantity'
        }

        with self.assertRaises(KeyError):
            Product.new_product(incomplete_data)
