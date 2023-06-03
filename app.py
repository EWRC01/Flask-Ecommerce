from flask import Flask, render_template, request, jsonify, redirect
import json

app = Flask(__name__)

# Mock product data
products = [
    {"id": 1, "name": "Auditoría", "price": 1000, "description": "Auditoría de infraestructura, Auditoría Web, Auditoría Física"},
    {"id": 2, "name": "Capacitación", "price": 500, "description": "Certificate con cualquiera de nuestros sponsors y logra tu objetivo"},
    {"id": 3, "name": "Desarrollo de Software", "price": 1200, "description": "Contáctanos, comentanos tus ideas y vuelvelas realidad"},
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', cart=cart)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/', methods=['POST'])
def add_to_cart():
    product_id = int(request.form.get('product_id'))
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        return jsonify(product)
    else:
        return jsonify(error="Product not found"), 404

@app.route('/clean', methods=['POST'])
def clean_cart():
    cart.clear()
    return jsonify(message="Cart cleaned")

@app.route('/checkout', methods=['POST'])
def checkout():
    return jsonify({'message': 'Pago Completado!'})