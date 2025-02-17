import random
from product_manager import ProductManager
from cart import Cart

# Crează o instanță a clasei ProductManager
manager = ProductManager()

# Crează o instanță a clasei Cart
cart = Cart()

# Selectează aleatoriu 3 produse din lista de produse disponibile
products_to_add = random.sample(manager.products, 3)

# Adaugă produsele selectate în coș cu cantitatea de 1 pentru fiecare
for product in products_to_add:
    cart.add_to_cart(product, 1)

# Modifică denumirile produselor sau cantitățile, dacă este necesar
cart.cart_items[0]['product'].name = "Updated Product Name"  # Schimbă numele unui produs
cart.cart_items[1]['quantity'] = 2  # Schimbă cantitatea unui produs

# Șterge liniile de cod legate de afișarea produsului și valoarea totală a inventarului
# cart.display_cart()  # Înlătură această linie, dacă vrei să elimini afișarea produselor
# print(f"\nTotal value of the cart: {cart.total_value()}")  # Înlătură această linie, dacă vrei să elimini valoarea totală
