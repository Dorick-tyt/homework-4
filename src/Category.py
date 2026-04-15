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
            products: Список товаров в категории (объекты Product)
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
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
            Строка с перечнем товаров, каждый товар на новой строке
        """
        if not self.__products:
            return "В категории нет товаров"

        return "\n".join(str(product) for product in self.__products)

    @property
    def total_cost(self) -> float:
        """
        Общая стоимость всех товаров в категории

        Returns:
            Сумма общей стоимости всех продуктов в категории
        """
        return sum(product.total_cost for product in self.__products)

    @property
    def products_count(self) -> int:
        """
        Общее количество единиц товаров в категории

        Returns:
            Сумма quantity всех продуктов
        """
        return sum(product.quantity for product in self.__products)

    def __str__(self) -> str:
        """
        Строковое отображение категории

        Returns:
            Строка в формате: "Название категории, количество продуктов: X шт."
        """
        return f"{self.name}, количество продуктов: {self.products_count} шт."

    def __add__(self, other):
        """
        Сложение категорий (общая стоимость товаров)

        Args:
            other: Другая категория или число

        Returns:
            Общая стоимость товаров в обеих категориях

        Raises:
            TypeError: Если other не является Category или числом
        """
        if isinstance(other, Category):
            # Суммируем общую стоимость двух категорий
            return self.total_cost + other.total_cost
        elif isinstance(other, (int, float)):
            # Если складываем с числом
            return self.total_cost + other
        else:
            raise TypeError(f"Нельзя сложить Category с типом {type(other).__name__}")

    def __radd__(self, other):
        """
        Правое сложение (для поддержки sum() и случаев, когда Category справа)

        Args:
            other: Другой объект (число или Category)

        Returns:
            Общая стоимость
        """
        if other == 0:
            # Для поддержки sum() с пустым начальным значением
            return self.total_cost
        return self.__add__(other)
