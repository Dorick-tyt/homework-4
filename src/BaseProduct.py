from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Конструктор базового класса

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество на складе
        """
        # Вызываем конструктор следующего класса в MRO
        super().__init__()
        # Сохраняем параметры для использования в дочерних классах
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для получения цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        """Абстрактный сеттер для установки цены"""
        pass

    @property
    @abstractmethod
    def total_cost(self) -> float:
        """Абстрактное свойство для общей стоимости товара"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод сложения продуктов"""
        pass

    @abstractmethod
    def __radd__(self, other):
        """Абстрактный метод правого сложения"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: Dict[str, Any]):
        """Абстрактный класс-метод для создания продукта из словаря"""
        pass
