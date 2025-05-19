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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product):
        required_keys = {'name', 'price', 'description', 'quantity'}
        if not all(key in product for key in required_keys):
            raise ValueError("В словаре должны быть ключи: name, price, description, quantity")
        return cls(
            name=product['name'],
            price=product['price'],
            description=product['description'],
            quantity=product['quantity']
        )

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
        self.__products = products
        Category.category_count += 1
        Category.product_count = len(products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)

    @property
    def products(self):
        if not self.__products:
            return "Список товаров пуст."
        return "\n".join(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                         for product in self.__products)

