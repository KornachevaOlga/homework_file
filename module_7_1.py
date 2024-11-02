import os

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self, name):
        self.name = name
        self.file_name = 'products.txt'

    def get_products(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                return content

    def add(self, *products):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            content = self.get_products()
            for product in products:
                tovar = f"{product}\n"
                if tovar in content:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(f"{product}\n")


# Создаем объекты
s1 = Shop("My Grocery Store")

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
print(p1)
print(p2)
print(p3)
print(p2)
s1.add(p1, p2, p3)

print(s1.get_products())






