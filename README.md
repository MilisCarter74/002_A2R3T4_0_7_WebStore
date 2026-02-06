# WebStore

## Description

**WebStore** is a simple Python-based website for demonstration of work regular store websites and especially mechanics of operations with goods. The website have simple CSS and html-based graphical interface of main page and cart page for imitation of buying goods. All operations with products are performed via class.

---

## Features

- Selecting and adding products to the cart
- Edditing the quantity of goods in the cart
- displaying the status of the products (out of stock / in stock)
- calculating the total amount in the cart

---

## Requirements

- Python 3.8+
- `flask` library
- `random` (included with most Python installations)

---

## Instalation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mistlp74/004_A2R3T4_0_3_PyMessenger.git
    cd WebStore
    ```

2. **Install dependencies:**
    ```bash
    pip install flask
    ```
   
---

## Usage

1. **Start the server** 
    ```bash
    python server.py
   ```

2. **Go to the website**  
   follow the link in the terminal or use another method to acces the site

---

## Project Structure

- `server.py` - Handle all server operations
- `product.py` - operations with goods
- `cart.html` - interface and logic for the cart page
- `shop.html` - interface and logic for the main page
- `shop.css` - styles for the main page

---

## Troubleshooting

- **Wrong total amount in the cart**

    Check displaying the number in cart.html or calculation in server.py (`def cart`)

---

## Author

Developed by [Milis Carter](https://github.com/MilisCarter74)
