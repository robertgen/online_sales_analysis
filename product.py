class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def display_info(self):
        print(f"Name: {self.name}, price: {self.price}, quantity: {self.quantity}")
    def update_quantity(self, quantity):
        if self.quantity + quantity >= 0:
            self.quantity += quantity
        else:
            print("Error: Not enough stock!")