from typing import List
from src.BaseProduct import BaseProduct


class Category:
    """Класс для представления категории товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[BaseProduct]):
        """
        Инициализация категории

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории (объекты BaseProduct и его наследников)
        """
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

        for product in products:
            self.add_product(product)

    def add_product(self, product: BaseProduct):
        """
        Добавляет товар в категорию с проверкой типа и количества

        Args:
            product: Объект класса BaseProduct или его наследника

        Raises:
            TypeError: Если product не является экземпляром BaseProduct
            ValueError: Если количество товара равно 0 или отрицательное
        """
        if not isinstance(product, BaseProduct):
            raise TypeError(
                f"Можно добавлять только объекты класса BaseProduct или его наследников. "
                f"Получен тип: {type(product).__name__}"
            )

        # Проверка количества товара
        if product.quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.__products.append(product)
        Category.product_count += 1

    def average_price(self) -> float:
        """
        Подсчитывает среднюю цену всех товаров в категории

        Returns:
            Средняя цена товара (сумма цен всех товаров / количество товаров)
            Если в категории нет товаров, возвращает 0

        Note:
            Для расчёта используется цена за единицу товара (price),
            а не общая стоимость (total_cost)
        """
        try:
            # Считаем сумму цен всех товаров
            total_price = sum(product.price for product in self.__products)
            # Считаем количество товаров
            products_count = len(self.__products)
            # Вычисляем среднюю цену
            return total_price / products_count
        except ZeroDivisionError:
            # Если в категории нет товаров, возвращаем 0
            return 0

    def average_cost(self) -> float:
        """
        Альтернативный метод: подсчитывает среднюю общую стоимость товаров

        Returns:
            Средняя общая стоимость (total_cost / количество товаров)
            Если в категории нет товаров, возвращает 0
        """
        try:
            total_cost = sum(product.total_cost for product in self.__products)
            products_count = len(self.__products)
            return total_cost / products_count
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в виде строки"""
        if not self.__products:
            return "В категории нет товаров"
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[BaseProduct]:
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