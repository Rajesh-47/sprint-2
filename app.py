from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Route for T-shirts page
@app.route('/tshirts')
def tshirts():
    return render_template('tshirts.html')

# Route for Bags page
@app.route('/bags')
def bags():
    return render_template('bags.html')

# Route for Cups page
@app.route('/cups')
def cups():
    return render_template('cups.html')

# Route for Cart page
@app.route('/cart')
def cart():
    # For simplicity, we'll add static cart items for now
    cart_items = [
        {"name": "T-shirt", "quantity": 1, "price": 20},
        {"name": "Bag", "quantity": 2, "price": 15}
    ]
    return render_template('cart.html', cart_items=cart_items)

# Route for Checkout page
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run()
