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
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self) -> float:
        """
        Геттер для получения цены товара

        Returns:
            Цена товара
        """
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        Сеттер для установки цены товара с проверкой

        Args:
            value: Новая цена товара
        """
        # Проверка на отрицательную или нулевую цену
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Проверка на понижение цены
        if value < self.__price:
            print(f"Вы пытаетесь понизить цену с {self.__price} до {value}")
            user_input = input("Вы уверены? (y/n): ").lower()

            if user_input in ["y", "yes", "да", "+", "1"]:
                self.__price = value
                print("Цена успешно изменена")
            else:
                print("Изменение цены отменено")
        else:
            # Повышение цены или оставление без изменений
            self.__price = value
            print(f"Цена успешно изменена на {value}")

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
