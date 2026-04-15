class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта (может быть с копейками)
            quantity: Количество в наличии (в штуках)
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для получения цены товара"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для установки цены товара с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            print(f"Вы пытаетесь понизить цену с {self.__price} до {value}")
            user_input = input("Вы уверены? (y/n): ").lower()

            if user_input == "y":
                self.__price = value
                print("Цена успешно изменена")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = value
            print(f"Цена успешно изменена на {value}")

    @property
    def total_cost(self) -> float:
        """
        Общая стоимость товара на складе

        Returns:
            price * quantity
        """
        return self.__price * self.quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового продукта из словаря

        Args:
            product_data: Словарь с ключами:
                - 'name': название товара
                - 'description': описание товара
                - 'price': цена товара
                - 'quantity': количество товара

        Returns:
            Объект класса Product
        """
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    def __str__(self) -> str:
        """
        Строковое отображение продукта

        Returns:
            Строка в формате: "Название продукта, X руб. Остаток: X шт."
        """
        price_int = int(self.__price) if self.__price.is_integer() else self.__price
        return f"{self.name}, {price_int} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение продуктов (общая стоимость товаров на складе)

        Args:
            other: Другой объект Product или число

        Returns:
            Общая стоимость: (price1 * quantity1) + (price2 * quantity2)

        Raises:
            TypeError: Если other не является Product или числом
        """
        if isinstance(other, Product):
            # Суммируем общую стоимость двух товаров
            return self.total_cost + other.total_cost
        elif isinstance(other, (int, float)):
            # Если складываем с числом
            return self.total_cost + other
        else:
            raise TypeError(f"Нельзя сложить Product с типом {type(other).__name__}")

    def __radd__(self, other):
        """
        Правое сложение (для поддержки sum() и случаев, когда Product справа)

        Args:
            other: Другой объект (число или Product)

        Returns:
            Общая стоимость
        """
        if other == 0:
            # Для поддержки sum() с пустым начальным значением
            return self.total_cost
        return self.__add__(other)
