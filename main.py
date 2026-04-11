from src.Product import Product
from src.Category import Category

if __name__ == "__main__":
    # Создаём продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаём категорию
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Выводим список товаров в категории (через геттер)
    print(category1.products)

    # Добавляем новый товар
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    # Снова выводим список товаров
    print(category1.products)

    # Выводим общее количество товаров во всех категориях
    print(category1.product_count)

    # Исправленный вызов new_product (передаём параметры отдельно, НЕ словарь)
    new_product = Product.new_product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    # Тестируем сеттер с корректной ценой
    new_product.price = 800
    print(new_product.price)

    # Тестируем сеттер с отрицательной ценой
    new_product.price = -100
    print(new_product.price)

    # Тестируем сеттер с нулевой ценой
    new_product.price = 0
    print(new_product.price)