#атрибуты #типы_данных #создание_класса #class
class Product:
    quantity = int  # Атрибут класса
    name: str  # Атрибуты (свойства) класса
    description: str
    price: float


    def __init__(self, name, description, price, quantity):
        """Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0


    def __init__(self, name, description, products):
        """Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
