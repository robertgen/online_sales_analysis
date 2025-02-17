from product import Product
class ProductManager:
    def __init__(self):
        self.products = [
            Product("Laptop", 1000, 50),
            Product("Keyboard", 400, 120),
            Product("Mouse", 150, 150),
            Product("Airpods", 430, 10),
            Product("Charges", 540, 87)
        ]
    def display_all_products(self):
        for product in self.products:
            product.display_info()
    def total_value(self):
        total = 0
        for j in self.products:
            total += j[1] * j[2]
        return total
    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
               
    
