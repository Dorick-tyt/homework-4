from typing import List

from src.Product import Product


class Category:
    """Класс для представления категории товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализация категории

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории (объекты Product и его наследников)
        """
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

        # Добавляем продукты через метод add_product для валидации
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию с проверкой типа

        Args:
            product: Объект класса Product или его наследника

        Raises:
            TypeError: Если product не является экземпляром Product или его наследника
        """
        # Проверяем, является ли product экземпляром Product или его наследником
        if not isinstance(product, Product):
            raise TypeError(
                f"Можно добавлять только объекты класса Product или его наследников. "
                f"Получен тип: {type(product).__name__}"
            )

        # Добавляем продукт
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в виде строки"""
        if not self.__products:
            return "В категории нет товаров"
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Геттер для получения списка товаров (только для чтения)"""
        return self.__products.copy()

    @property
    def total_cost(self) -> float:
        """Общая стоимость всех товаров в категории"""
        return sum(product.total_cost for product in self.__products)

    @property
    def products_count(self) -> int:
        """Общее количество единиц товаров в категории"""
        return sum(product.quantity for product in self.__products)

    def __str__(self) -> str:
        """Строковое отображение категории"""
        return f"{self.name}, количество продуктов: {self.products_count} шт."

    def __add__(self, other):
        """Сложение категорий (общая стоимость товаров)"""
        if isinstance(other, Category):
            return self.total_cost + other.total_cost
        elif isinstance(other, (int, float)):
            return self.total_cost + other
        else:
            raise TypeError(f"Нельзя сложить Category с типом {type(other).__name__}")

    def __radd__(self, other):
        """Правое сложение (для поддержки sum())"""
        if other == 0:
            return self.total_cost
        return self.__add__(other)
