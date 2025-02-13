# Online Sales Analysis

Acest proiect simulează gestionarea unui magazin online, cu funcționalități de gestionare a produselor, coșului de cumpărături și actualizarea stocurilor. Proiectul include mai multe clase care permit adăugarea, actualizarea și afișarea produselor, precum și gestionarea coșului de cumpărături.

## Clase implementate

### 1. **Product**
Clasa `Product` reprezintă un produs disponibil pentru vânzare în magazinul online.

Atribute:
- `name`: Numele produsului.
- `price`: Prețul produsului.
- `quantity`: Cantitatea disponibilă a produsului.

Metode:
- `display_info()`: Afișează informațiile despre produs.
- `update_quantity()`: Actualizează cantitatea unui produs.

### 2. **ProductManager**
Clasa `ProductManager` gestionează o listă de produse disponibile.

Atribute:
- `products`: O listă cu produsele disponibile (sub forma unui obiect `Product`).

Metode:
- `add_product()`: Adaugă un produs în lista de produse.
- `remove_product()`: Îndepărtează un produs din lista de produse.
- `display_all_products()`: Afișează toate produsele disponibile.
- `total_inventory_value()`: Calculează valoarea totală a tuturor produselor disponibile.

### 3. **Cart**
Clasa `Cart` gestionează coșul de cumpărături al unui client.

Atribute:
- `cart_items`: O listă de produse adăugate în coș (fiecare produs este însoțit de cantitatea sa).

Metode:
- `add_to_cart()`: Adaugă un produs în coș.
- `total_value()`: Calculează valoarea totală a coșului de cumpărături.
- `display_cart()`: Afișează produsele din coș și cantitățile acestora.

## Funcționalități implementate

- **Adăugare produse**: Produsele pot fi adăugate la lista de produse disponibile și la coșul de cumpărături.
- **Actualizare stocuri**: Cantitatea unui produs poate fi actualizată.
- **Calcularea valorii totale**: Valoarea totală a produselor disponibile și a coșului de cumpărături poate fi calculată.
- **Gestionarea coșului de cumpărături**: Produsele pot fi adăugate sau îndepărtate din coș.

## Instrucțiuni de utilizare

1. Clasa `ProductManager` poate fi utilizată pentru a adăuga, elimina și vizualiza produsele.
2. Clasa `Cart` poate fi utilizată pentru a adăuga produse în coș și a calcula valoarea totală a coșului.
3. Codul se bazează pe un fișier `config.json` pentru a stoca informații sensibile care sunt ignorate în Git folosind `.gitignore`.

## Tehnologii utilizate

- Python 3.x
- Git
- GitHub
