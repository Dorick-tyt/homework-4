import unittest
from src.LawnGrass import LawnGrass
from src.Product import Product


class TestLawnGrass(unittest.TestCase):
    """Тесты для класса LawnGrass"""

    def setUp(self):
        """Подготовка данных для тестов"""
        self.grass = LawnGrass(
            "Газонная смесь 'Изумруд'",
            "Быстрорастущая газонная трава для спортивных полей",
            1500.0,
            20,
            "Германия",
            14,
            "Тёмно-зелёный"
        )

    def test_lawn_grass_creation(self):
        """Тест создания газонной травы"""
        self.assertEqual(self.grass.name, "Газонная смесь 'Изумруд'")
        self.assertEqual(self.grass.description, "Быстрорастущая газонная трава для спортивных полей")
        self.assertEqual(self.grass.price, 1500.0)
        self.assertEqual(self.grass.quantity, 20)
        self.assertEqual(self.grass.country, "Германия")
        self.assertEqual(self.grass.germination_period, 14)
        self.assertEqual(self.grass.color, "Тёмно-зелёный")

    def test_lawn_grass_inheritance(self):
        """Тест наследования от Product"""
        self.assertIsInstance(self.grass, Product)
        self.assertTrue(issubclass(LawnGrass, Product))

    def test_lawn_grass_total_cost(self):
        """Тест расчета общей стоимости"""
        expected_cost = 1500.0 * 20
        self.assertEqual(self.grass.total_cost, expected_cost)

    def test_lawn_grass_price_setter(self):
        """Тест изменения цены травы"""
        old_price = self.grass.price

        # Попытка установить отрицательную цену
        self.grass.price = -500
        self.assertEqual(self.grass.price, old_price)

    def test_lawn_grass_str(self):
        """Тест строкового представления"""
        str_repr = str(self.grass)
        self.assertIn("Газонная смесь 'Изумруд'", str_repr)
        self.assertIn("1500", str_repr)
        self.assertIn("Остаток: 20 шт.", str_repr)
        self.assertIn("Газонная трава", str_repr)
        self.assertIn("Германия", str_repr)
        self.assertIn("14 дней", str_repr)
        self.assertIn("Тёмно-зелёный", str_repr)

    def test_lawn_grass_addition_same_type(self):
        """Тест сложения двух товаров одного типа"""
        grass2 = LawnGrass(
            "Трава 'Мавританский газон'",
            "Смесь злаков",
            2500.0,
            10,
            "Нидерланды",
            21,
            "Зелёный"
        )
        result = self.grass + grass2
        expected = (1500.0 * 20) + (2500.0 * 10)
        self.assertEqual(result, expected)

    def test_lawn_grass_addition_different_type(self):
        """Тест сложения травы со смартфоном (должен вызвать ошибку)"""
        from src.Smartphone import Smartphone
        smartphone = Smartphone(
            "Phone", "Desc", 50000.0, 3,
            "Высокая", "M1", 128, "Черный"
        )

        with self.assertRaises(TypeError) as context:
            _ = self.grass + smartphone
        self.assertIn("Нельзя складывать товары разных классов", str(context.exception))
