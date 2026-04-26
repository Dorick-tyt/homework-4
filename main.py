from src.Product import Product
from src.Smartphone import Smartphone
from src.LawnGrass import LawnGrass
from src.Category import Category

if __name__ == '__main__':


    print("=" * 60)
    print("ПРОВЕРКА СОЗДАНИЯ ТОВАРА С НУЛЕВЫМ КОЛИЧЕСТВОМ")
    print("=" * 60)

    # Проверка создания товара с нулевым количеством
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
    except ValueError as e:
        print(f"✓ Возникла ошибка ValueError: {e}")
        print("Программа прервана для этого товара, но продолжает работу для остальных")

    print("\n" + "=" * 60)
    print("СОЗДАНИЕ КОРРЕКТНЫХ ТОВАРОВ")
    print("=" * 60)

    # Создание корректных товаров
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(f"✓ Созданы товары:")
    print(f"  - {product1.name}, количество: {product1.quantity}")
    print(f"  - {product2.name}, количество: {product2.quantity}")
    print(f"  - {product3.name}, количество: {product3.quantity}")

    print("\n" + "=" * 60)
    print("КАТЕГОРИЯ С ТОВАРАМИ")
    print("=" * 60)

    # Создание категории с товарами
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(f"Категория: {category1}")
    print(f"\nСписок товаров:")
    print(category1.products)

    # Вызов метода middle_price (average_price)
    print(f"\nСредняя цена товаров: {category1.average_price():.2f} руб.")
    print(f"Количество товаров в категории: {len(category1.products_list)}")
    print(f"Общее количество единиц: {category1.products_count} шт.")

    print("\n" + "=" * 60)
    print("ПУСТАЯ КАТЕГОРИЯ")
    print("=" * 60)

    # Создание пустой категории
    category_empty = Category("Пустая категория", "Категория без продуктов", [])

    print(f"Категория: {category_empty}")
    print(f"Средняя цена (пустая категория): {category_empty.average_price()} руб.")
    print(f"Количество товаров: {len(category_empty.products_list)}")

    print("\n" + "=" * 60)
    print("ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ")
    print("=" * 60)

    # Проверка создания товара с отрицательным количеством
    try:
        product_negative = Product("Отрицательный товар", "Отрицательное количество", 1000.0, -5)
        print("Не возникла ошибка ValueError при попытке добавить продукт с отрицательным количеством")
    except ValueError as e:
        print(f"✓ Возникла ошибка ValueError при отрицательном количестве: {e}")

    # Проверка работы average_price с разными типами товаров
    smartphone = Smartphone(
        "iPhone 15 Pro", "Флагман", 120000.0, 3,
        "Высокая", "15 Pro", 256, "Черный"
    )

    grass = LawnGrass(
        "Газон 'Изумруд'", "Элитная трава", 2000.0, 10,
        "Германия", 14, "Зелёный"
    )

    mixed_category = Category(
        "Смешанная категория",
        "Товары разных типов",
        [product1, smartphone, grass]
    )

    print(f"\nСмешанная категория: {mixed_category}")
    print(f"Средняя цена: {mixed_category.average_price():.2f} руб.")
    print(f"Средняя общая стоимость: {mixed_category.average_cost():.2f} руб.")