from flask import Flask, jsonify, render_template, request, redirect
from product import Product, add_to_storage, add_to_basket, storage, basket, generate_user_key

app = Flask(__name__, static_folder="static", template_folder="templates")

add_to_storage(Product(1, 1200, 5, "notebook", "Images/product_7497285.jpg"))
add_to_storage(Product(2, 35, 0, "mouse", "Images/product_6371464.jpg"))
add_to_storage(Product(3, 300, 2, "monitor 24 inches", "Images/product_6261370.jpg"))
add_to_storage(Product(4, 150, 10, "keyboard RGB", "Images/product_7346020.jpg"))

@app.route("/")
def redirect_to_user():
    key = generate_user_key()
    return redirect(f"/{key}")

@app.route("/<user_key>")
def shop(user_key):
    return render_template("shop.html", user_key=user_key, products=storage)

@app.route("/add_to_basket", methods=["POST"])
def add():
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = int(data.get("quantity", 1))
    success = add_to_basket(product_id, quantity)
    return jsonify({"success": success})

@app.route("/cart/<user_key>")
def cart(user_key):
    basket_products = []
    total = 0
    for item in basket:
        prod = next((p for p in storage if p.id == item['product_id']), None)
        if prod:
            subtotal = prod.price * item['quantity']
            total += subtotal
            basket_products.append({
                "id": prod.id,
                "description": prod.description,
                "price": prod.price,
                "amount": prod.amount,
                "photo": prod.photo,
                "quantity": item['quantity']
            })
    return render_template("cart.html", user_key=user_key, basket=basket_products, total=total)

@app.route("/update_basket", methods=["POST"])
def update_basket():
    data = request.get_json()
    product_id = int(data.get("product_id"))
    quantity = data.get("quantity")
    action = data.get("action")

    global basket
    if action == "remove":
        basket = [item for item in basket if item['product_id'] != product_id]
        return jsonify({"success": True})

    elif action == "update":
        prod = next((p for p in storage if p.id == product_id), None)
        if prod and quantity is not None and 0 < int(quantity) <= prod.amount:
            for item in basket:
                if item['product_id'] == product_id:
                    item['quantity'] = int(quantity)
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "error": "insufficient quantity in stock"})
    return jsonify({"success": False, "error": "Incorrect action"})


if __name__ == "__main__":
    app.run(debug=True)