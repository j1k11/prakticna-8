class Shop:
    def __init__(self, name, category, location):
        self.name = name
        self.category = category
        self.location = location

    def display_info(self):
        print(f"Shop: {self.name}\nCategory: {self.category}\nLocation: {self.location}\n")


class Customer:
    def __init__(self, name, age, budget):
        self.name = name
        self.age = age
        self.budget = budget

    def display_info(self):
        print(f"Customer: {self.name}\nAge: {self.age}\nBudget: ${self.budget}\n")


class ShoppingMall:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.shops = []

    def add_shop(self, shop):
        self.shops.append(shop)

    def display_shops(self):
        print(f"Shops in {self.name}:")
        for shop in self.shops:
            shop.display_info()


# Example Usage:
mall = ShoppingMall("Електроніка Світу", "Книги")

shop1 = Shop("Електроніка Світу", "Електроніка", "Поверх 1")
shop2 = Shop("Мода Раю", "Одяг", "Поверх 2")
shop3 = Shop("Книжковий Рай", "Книги", "Поверх 3")

mall.add_shop(shop1)
mall.add_shop(shop2)
mall.add_shop(shop3)

customer1 = Customer("віка", 28, 1000)
customer2 = Customer("ваня", 35, 1500)

customer1.display_info()
customer2.display_info()

mall.display_shops()
