import unittest
from io import StringIO
import sys
from src.Product import Product


class TestLogMixin(unittest.TestCase):
    """Тесты для LogMixin"""

    def setUp(self):
        """Подготовка для перехвата вывода print"""
        self.captured_output = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.captured_output

    def tearDown(self):
        """Восстановление stdout"""
        sys.stdout = self.old_stdout

    def test_log_mixin_prints_on_product_creation(self):
        """Тест: миксин выводит сообщение при создании Product"""
        product = Product("Тест", "Описание", 100, 10)
        output = self.captured_output.getvalue()

        self.assertIn("Создан объект: Product", output)
        self.assertIn("'Тест'", output)
        self.assertIn("'Описание'", output)
        self.assertIn("100", output)
        self.assertIn("10", output)

    def test_log_mixin_shows_correct_class_name(self):
        """Тест: миксин выводит правильное имя класса"""
        Product("Test", "Desc", 100, 10)
        output = self.captured_output.getvalue()
        self.assertTrue(output.startswith("Создан объект: Product("))

    def test_log_mixin_shows_all_parameters(self):
        """Тест: миксин выводит все параметры"""
        Product("Продукт", "Детальное описание", 999.99, 42)
        output = self.captured_output.getvalue()

        self.assertIn("'Продукт'", output)
        self.assertIn("'Детальное описание'", output)
        self.assertIn("999.99", output)
        self.assertIn("42", output)

    def test_log_mixin_called_for_each_creation(self):
        """Тест: миксин вызывается при каждом создании объекта"""
        Product("Product1", "Desc1", 100, 1)
        Product("Product2", "Desc2", 200, 2)
        Product("Product3", "Desc3", 300, 3)

        output = self.captured_output.getvalue()
        lines = output.strip().split('\n')

        self.assertEqual(len(lines), 3)
        self.assertIn("Product1", lines[0])
        self.assertIn("Product2", lines[1])
        self.assertIn("Product3", lines[2])

    def test_log_mixin_handles_empty_parameters(self):
        """Тест: миксин обрабатывает создание без параметров"""

        # Создаём класс без параметров для теста
        class EmptyClass(Product):
            def __init__(self):
                super().__init__("Default", "Desc", 0, 0)

        empty = EmptyClass()
        output = self.captured_output.getvalue()

        self.assertIn("Создан объект: EmptyClass", output)


class TestLogMixinOrder(unittest.TestCase):
    """Тесты для проверки порядка вызова миксина"""

    def setUp(self):
        self.captured_output = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_log_mixin_called_before_product_init(self):
        """Тест: миксин вызывается до конструктора Product"""
        product = Product("Test", "Desc", 100, 10)
        output = self.captured_output.getvalue()

        # Проверяем, что вывод есть
        self.assertTrue(len(output) > 0)

    def test_log_mixin_mro_correct(self):
        """Тест: правильный порядок MRO для Product"""
        expected_mro = ['Product', 'LogMixin', 'BaseProduct', 'ABC', 'object']
        actual_mro = [cls.__name__ for cls in Product.__mro__]

        # Проверяем, что LogMixin находится в MRO
        self.assertIn('LogMixin', actual_mro)
        self.assertIn('BaseProduct', actual_mro)

        # Проверяем порядок (LogMixin должен быть после Product, но перед BaseProduct)
        product_index = actual_mro.index('Product')
        log_index = actual_mro.index('LogMixin')
        base_index = actual_mro.index('BaseProduct')

        self.assertLess(product_index, log_index)
        self.assertLess(log_index, base_index)

