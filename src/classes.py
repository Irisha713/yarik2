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


    def __str__(self):
        return f"{self.name}, {self.price} руб. остаток: {self.quantity} шт."


    def __add__(self, other):
        if isinstance(self, type(other)):
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError


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
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        if not self.__products:
            return "Список товаров пуст."
        return "\n".join(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                         for product in self.__products)


    def __str__(self):
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
