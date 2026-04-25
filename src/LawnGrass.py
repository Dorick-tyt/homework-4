# src/LawnGrass.py
from src.Product import Product


class LawnGrass(Product):
    """Класс для представления газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        # Передаём все параметры в родительский класс
        super().__init__(name, description, price, quantity)

        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Строковое отображение газонной травы"""
        base_str = super().__str__()
        return f"{base_str} (Газонная трава: {self.country}, всходы через {self.germination_period} дней, {self.color})"
