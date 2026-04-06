import unittest
from src.Product import Product
from src.Category import Category


class TestCategory(unittest.TestCase):
    """Тесты для класса Category"""

    def setUp(self):
        """Подготовка данных для тестов"""
        # Сбрасываем счетчики перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0

        # Создаем продукты
        self.product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        self.product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    def test_category_with_empty_products(self):
        """Тест категории с пустым списком продуктов"""
        category = Category("Пустая категория", "Описание пустой категории", [])

        self.assertEqual(category.name, "Пустая категория")
        self.assertEqual(len(category.products), 0)

    def test_category_count_increment(self):
        """Тест правильного подсчета количества категорий"""
        # Сбрасываем счетчик
        Category.category_count = 0

        category1 = Category("Категория 1", "Описание 1", [])
        self.assertEqual(Category.category_count, 1)

        category2 = Category("Категория 2", "Описание 2", [])
        self.assertEqual(Category.category_count, 2)

        category3 = Category("Категория 3", "Описание 3", [])
        self.assertEqual(Category.category_count, 3)

    def test_product_count_increment(self):
        """Тест правильного подсчета количества продуктов"""
        # Сбрасываем счетчик
        Category.product_count = 0

        category1 = Category("Категория 1", "Описание 1", [self.product1])
        self.assertEqual(Category.product_count, 1)

        category2 = Category(
            "Категория 2", "Описание 2", [self.product2, self.product3]
        )
        self.assertEqual(Category.product_count, 3)  # 1 + 2 = 3

        category3 = Category("Категория 3", "Описание 3", [self.product4])
        self.assertEqual(Category.product_count, 4)  # 3 + 1 = 4

    def test_multiple_categories_with_products(self):
        """Тест подсчета продуктов в нескольких категориях"""
        Category.category_count = 0
        Category.product_count = 0

        cat1 = Category(
            "Смартфоны", "Описание", [self.product1, self.product2, self.product3]
        )
        cat2 = Category("Телевизоры", "Описание", [self.product4])

        self.assertEqual(Category.category_count, 2)
        self.assertEqual(Category.product_count, 4)  # 3 + 1 = 4

    def test_category_products_list_type(self):
        """Тест типа данных списка продуктов"""
        category = Category("Тест", "Описание", [self.product1, self.product2])
        self.assertIsInstance(category.products, list)
        self.assertIsInstance(category.products[0], Product)

    def test_category_description_type(self):
        """Тест типа данных описания категории"""
        category = Category("Тест", "Описание", [])
        self.assertIsInstance(category.description, str)

    def test_category_count_is_class_attribute(self):
        """Тест, что category_count является атрибутом класса"""
        cat1 = Category("Кат1", "Описание", [])
        cat2 = Category("Кат2", "Описание", [])

        # Атрибут класса одинаков для всех экземпляров
        self.assertEqual(cat1.category_count, Category.category_count)
        self.assertEqual(cat2.category_count, Category.category_count)
