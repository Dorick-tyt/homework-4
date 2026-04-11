from typing import List
from src.Product import Product


class Category:
    """Класс для представления категории товаров"""

    # Атрибуты класса
    category_count = 0  # Общее количество категорий (переименовано)
    product_count = 0  # Общее количество товаров (переименовано)

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализация категории

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории (объекты Product)
        """
        self.name = name
        self.description = description
        self.__products = products

        # Увеличиваем количество категорий
        Category.category_count += 1

        # Увеличиваем количество товаров на количество продуктов в категории
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию

        Args:
            product: Объект класса Product для добавления
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для получения списка товаров в виде строки

        Returns:
            Строка с перечнем товаров в формате:
            "Название продукта, X руб. Остаток: Y шт."
        """
        if not self.__products:
            return "В категории нет товаров"

        result_lines = []
        for product in self.__products:
            # Предполагаем, что у класса Product есть атрибуты: name, price, quantity
            result_lines.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )

        return "\n".join(result_lines)
