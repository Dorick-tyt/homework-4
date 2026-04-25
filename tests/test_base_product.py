import unittest
from src.BaseProduct import BaseProduct
from src.Product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass


class TestBaseProduct(unittest.TestCase):
    """Тесты для абстрактного базового класса BaseProduct"""

    def test_cannot_instantiate_abstract_class(self):
        """Тест: нельзя создать экземпляр абстрактного класса"""
        with self.assertRaises(TypeError):
            BaseProduct("Test", "Desc", 100, 10)

    def test_product_is_subclass_of_baseproduct(self):
        """Тест: Product является наследником BaseProduct"""
        self.assertTrue(issubclass(Product, BaseProduct))

    def test_smartphone_is_subclass_of_baseproduct(self):
        """Тест: Smartphone является наследником BaseProduct"""
        self.assertTrue(issubclass(Smartphone, BaseProduct))

    def test_lawn_grass_is_subclass_of_baseproduct(self):
        """Тест: LawnGrass является наследником BaseProduct"""
        self.assertTrue(issubclass(LawnGrass, BaseProduct))

    def test_product_instance_is_baseproduct(self):
        """Тест: экземпляр Product является экземпляром BaseProduct"""
        product = Product("Test", "Desc", 100, 10)
        self.assertIsInstance(product, BaseProduct)

    def test_smartphone_instance_is_baseproduct(self):
        """Тест: экземпляр Smartphone является экземпляром BaseProduct"""
        smartphone = Smartphone("Phone", "Desc", 100, 1, "High", "M1", 128, "Black")
        self.assertIsInstance(smartphone, BaseProduct)

    def test_lawn_grass_instance_is_baseproduct(self):
        """Тест: экземпляр LawnGrass является экземпляром BaseProduct"""
        grass = LawnGrass("Grass", "Desc", 100, 1, "Russia", 7, "Green")
        self.assertIsInstance(grass, BaseProduct)

    def test_baseproduct_has_abstract_methods(self):
        """Тест: BaseProduct имеет абстрактные методы"""
        abstract_methods = ['__init__', '__str__', '__add__', '__radd__', 'new_product']

        for method in abstract_methods:
            self.assertTrue(
                hasattr(BaseProduct, method),
                f"BaseProduct должен иметь абстрактный метод {method}"
            )

    def test_baseproduct_has_abstract_properties(self):
        """Тест: BaseProduct имеет абстрактные свойства"""
        self.assertTrue(hasattr(BaseProduct, 'price'))
        self.assertTrue(hasattr(BaseProduct, 'total_cost'))

    def test_all_products_implement_required_methods(self):
        """Тест: все классы-продукты реализуют все методы BaseProduct"""
        product_classes = [Product, Smartphone, LawnGrass]
        required_methods = ['__str__', '__add__', '__radd__', 'new_product']

        for product_class in product_classes:
            for method in required_methods:
                self.assertTrue(
                    hasattr(product_class, method),
                    f"{product_class.__name__} должен реализовать метод {method}"
                )

    def test_all_products_have_required_properties(self):
        """Тест: все классы-продукты имеют свойства price и total_cost"""
        product_classes = [Product, Smartphone, LawnGrass]

        for product_class in product_classes:
            self.assertTrue(
                hasattr(product_class, 'price'),
                f"{product_class.__name__} должен иметь свойство price"
            )
            self.assertTrue(
                hasattr(product_class, 'total_cost'),
                f"{product_class.__name__} должен иметь свойство total_cost"
            )
