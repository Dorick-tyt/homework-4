class Product:
    """Базовый класс для представления продукта"""

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
        """Общая стоимость товара на складе"""
        return self.__price * self.quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания нового продукта из словаря"""
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    def __str__(self) -> str:
        """Строковое отображение продукта"""
        price_int = int(self.__price) if self.__price.is_integer() else self.__price
        return f"{self.name}, {price_int} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение продуктов (общая стоимость товаров на складе)

        Важно: можно складывать только товары одного класса!

        Args:
            other: Другой объект Product или его наследник

        Returns:
            Общая стоимость: (price1 * quantity1) + (price2 * quantity2)

        Raises:
            TypeError: Если other не является Product или типы товаров разные
        """
        # Проверяем, что other является экземпляром Product
        if not isinstance(other, Product):
            raise TypeError(f"Нельзя сложить Product с типом {type(other).__name__}")

        # Проверяем, что товары одного класса
        if not isinstance(other, type(self)):
            raise TypeError(
                f"Нельзя складывать товары разных классов: "
                f"{type(self).__name__} и {type(other).__name__}"
            )

        # Складываем общую стоимость
        return self.total_cost + other.total_cost

    def __radd__(self, other):
        """Правое сложение (для поддержки sum())"""
        if other == 0:
            return self.total_cost
        return self.__add__(other)
