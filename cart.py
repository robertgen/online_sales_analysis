class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):

        for item in self.cart_items:
            if item['product'].name == product.name:
                item['quantity'] += quantity
                print(f"Added {quantity} more {product.name} to cart.")
                return
        self.cart_items.append({'product': product, 'quantity': quantity})
        print(f"Added {quantity} {product.name} to cart.")
    def total_value(self):
        """Calculează valoarea totală a coșului."""
        total = 0
        for item in self.cart_items:
            total += item['product'].price * item['quantity']
        return total
    def display_cart(self):
        """Afișează produsele din coș și cantitățile acestora."""
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.cart_items:
                print(f"Name: {item['product'].name}, Price: {item['product'].price}, Quantity: {item['quantity']}")