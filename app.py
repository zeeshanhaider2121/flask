from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dummy in-memory storage (replace with vector DB)
doc_store = []


def simple_rag(query):
    context = "\n".join(doc_store[:3])
    return f"Answer based on docs: {context[:200]} ...\n\nQ: {query}"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")

def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/calculate")
def calculate():
    price = 200
    discount_percent = 10
    
    # INTENTIONAL BUG: This subtracts 10 from 100, instead of calculating 10% off.
    # Correct logic should be: price * (1 - discount_percent / 100)
    final_price = price - discount_percent 
    
    return f"Price: {price}, Discount: {discount_percent}%, Final: {final_price}"

if __name__ == "__main__":
    app.run(debug=True)