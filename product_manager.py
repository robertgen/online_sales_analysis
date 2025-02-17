class ProductManager:
    products = [
        ["Laptop", 1000, 50],
        ["Keyboard", 400, 120],
        ["Mouse", 150, 150],
        ["Airpods", 430, 10],
        ["Charges", 540, 87]
]
    def display_all_products(self):
        for i in self.products:
            print(f"Name: {i[0]}, Price: {i[1]}, Quantity: {i[2]}")
    def total_value(self):
        total = 0
        for j in self.products:
            total += j[1] * j[2]
        return total
    def add_product(self, name, price, quantity):
        self.products.append([name, price, quantity])
               
    