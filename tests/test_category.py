import unittest
from src.Product import Product
from src.Category import Category


class TestCategoryAdd(unittest.TestCase):
    """Тесты для магического метода __add__ в Category"""

    def setUp(self):
        self.product1 = Product("Товар A", "Описание", 100.0, 10)
        self.product2 = Product("Товар B", "Описание", 200.0, 5)
        self.product3 = Product("Товар C", "Описание", 50.0, 20)

        self.category1 = Category("Категория 1", "Описание", [self.product1, self.product2])
        self.category2 = Category("Категория 2", "Описание", [self.product3])

    def test_add_two_categories(self):
        """Тест сложения двух категорий"""
        result = self.category1 + self.category2
        # Категория 1: 100*10 + 200*5 = 1000 + 1000 = 2000
        # Категория 2: 50*20 = 1000
        # Итого: 3000
        self.assertEqual(result, 3000.0)

    def test_add_category_with_number(self):
        """Тест сложения категории с числом"""
        result = self.category1 + 500
        self.assertEqual(result, 2500.0)  # 2000 + 500 = 2500

    def test_total_cost_property(self):
        """Тест свойства total_cost"""
        self.assertEqual(self.category1.total_cost, 2000.0)
        self.assertEqual(self.category2.total_cost, 1000.0)

    def test_products_count_property(self):
        """Тест свойства products_count"""
        self.assertEqual(self.category1.products_count, 15)  # 10 + 5 = 15
        self.assertEqual(self.category2.products_count, 20)

    def test_sum_of_categories(self):
        """Тест sum() для списка категорий"""
        categories = [self.category1, self.category2]
        self.assertEqual(sum(categories), 3000.0)

    def test_add_invalid_type(self):
        """Тест сложения с неподдерживаемым типом"""
        with self.assertRaises(TypeError):
            _ = self.category1 + "invalid"

    def test_radd_with_initial_value(self):
        """Тест sum() с начальным значением"""
        categories = [self.category1, self.category2]
        self.assertEqual(sum(categories, 1000), 4000.0)  # 1000 + 3000 = 4000