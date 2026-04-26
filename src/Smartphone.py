from src.Product import Product


class Smartphone(Product):
    """Класс для представления смартфона"""

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: str,
            model: str,
            memory: int,
            color: str
    ):
        # Проверка количества будет выполнена в Product.__init__
        super().__init__(name, description, price, quantity)

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        """Строковое отображение смартфона"""
        base_str = super().__str__()
        return f"{base_str} (Смартфон: {self.model}, {self.memory}ГБ, {self.color})"