import unittest
from src.Smartphone import Smartphone
from src.Product import Product


class TestSmartphone(unittest.TestCase):
    """Тесты для класса Smartphone"""

    def setUp(self):
        """Подготовка данных для тестов"""
        self.smartphone = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "Флагманский смартфон с отличной камерой",
            180000.0,
            5,
            "Высокая",
            "SM-S918B",
            512,
            "Серый"
        )

    def test_smartphone_creation(self):
        """Тест создания смартфона"""
        self.assertEqual(self.smartphone.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(self.smartphone.description, "Флагманский смартфон с отличной камерой")
        self.assertEqual(self.smartphone.price, 180000.0)
        self.assertEqual(self.smartphone.quantity, 5)
        self.assertEqual(self.smartphone.efficiency, "Высокая")
        self.assertEqual(self.smartphone.model, "SM-S918B")
        self.assertEqual(self.smartphone.memory, 512)
        self.assertEqual(self.smartphone.color, "Серый")

    def test_smartphone_inheritance(self):
        """Тест наследования от Product"""
        self.assertIsInstance(self.smartphone, Product)
        self.assertTrue(issubclass(Smartphone, Product))

    def test_smartphone_total_cost(self):
        """Тест расчета общей стоимости"""
        expected_cost = 180000.0 * 5
        self.assertEqual(self.smartphone.total_cost, expected_cost)

    def test_smartphone_price_setter(self):
        """Тест изменения цены смартфона"""
        # Сохраняем старую цену
        old_price = self.smartphone.price

        # Пытаемся установить некорректную цену
        self.smartphone.price = -100
        self.assertEqual(self.smartphone.price, old_price)

        self.smartphone.price = 0
        self.assertEqual(self.smartphone.price, old_price)

    def test_smartphone_str(self):
        """Тест строкового представления"""
        str_repr = str(self.smartphone)
        self.assertIn("Samsung Galaxy S23 Ultra", str_repr)
        self.assertIn("180000", str_repr)
        self.assertIn("Остаток: 5 шт.", str_repr)
        self.assertIn("Смартфон", str_repr)
        self.assertIn("SM-S918B", str_repr)
        self.assertIn("512ГБ", str_repr)
        self.assertIn("Серый", str_repr)

    def test_smartphone_addition_same_type(self):
        """Тест сложения двух смартфонов"""
        smartphone2 = Smartphone(
            "iPhone 15 Pro",
            "Новейший iPhone",
            210000.0,
            8,
            "Максимальная",
            "A2848",
            256,
            "Черный"
        )
        result = self.smartphone + smartphone2
        expected = (180000.0 * 5) + (210000.0 * 8)
        self.assertEqual(result, expected)

    def test_smartphone_addition_different_type(self):
        """Тест сложения смартфона с другим типом (должен вызвать ошибку)"""
        from src.LawnGrass import LawnGrass
        grass = LawnGrass(
            "Трава", "Описание", 1000.0, 10,
            "Россия", 14, "Зеленый"
        )

        with self.assertRaises(TypeError) as context:
            _ = self.smartphone + grass
        self.assertIn("Нельзя складывать товары разных классов", str(context.exception))
