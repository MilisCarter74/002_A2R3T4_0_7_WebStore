import random
import string

storage = []
basket = []

class Product:
    def __init__(self, id, price, amount, description, photo):
        self.id = int(id)
        self.price = float(price)
        self.amount = int(amount)
        self.description = description
        self.photo = photo

    def is_available(self):
        return self.amount > 0

def add_to_storage(product: Product):
    storage.append(product)

def add_to_basket(product_id, quantity=1):
    product_id = int(product_id)
    prod = next((p for p in storage if p.id == product_id), None)
    if not prod:
        return False

    current_quantity = 0
    for item in basket:
        if item['product_id'] == product_id:
            current_quantity = item['quantity']
            break

    if current_quantity + quantity > prod.amount:
        return False

    for item in basket:
        if item['product_id'] == product_id:
            item['quantity'] += quantity
            return True

    basket.append({"product_id": product_id, "quantity": quantity})
    return True

def generate_user_key():
    return ''.join(random.choices(string.digits, k=6))