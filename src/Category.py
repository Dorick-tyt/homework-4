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
        self.products = products

        # Увеличиваем количество категорий
        Category.category_count += 1

        # Увеличиваем количество товаров на количество продуктов в категории
        Category.product_count += len(products)
