from flask import Flask

app = Flask(__name__)

# In-memory data storage for menu items
menu_items = [
    {"id": 1, "name": "Margherita Pizza", "price": 12.99, "description": "Classic tomato and mozzarella pizza"},
    {"id": 2, "name": "Cheeseburger", "price": 8.99, "description": "Juicy beef patty with melted cheese"},
    {"id": 3, "name": "Caesar Salad", "price": 7.99, "description": "Fresh romaine lettuce with Caesar dressing"},
]

@app.route('/')
def home():
    """Home page route"""
    return "<h1>Welcome to FastBites!</h1><p>Your favorite food delivery app.</p><a href='/menu'>View Menu</a>"

@app.route('/menu')
def menu():
    """Menu page route - displays all available food items"""
    items_html = ""
    for item in menu_items:
        items_html += f"<div><h3>{item['name']}</h3><p>{item['description']}</p><p>Price: ${item['price']}</p></div><hr>"
    
    return f"<h1>Our Menu</h1>{items_html}<a href='/'>Back to Home</a>"

@app.route('/item/<int:item_id>')
def item_detail(item_id):
    """Specific item page route - shows details for a single menu item"""
    # Find the item by ID
    item = None
    for menu_item in menu_items:
        if menu_item['id'] == item_id:
            item = menu_item
            break
    
    if item:
        return f"""
        <h1>{item['name']}</h1>
        <p>{item['description']}</p>
        <p><strong>Price:</strong> ${item['price']}</p>
        <a href='/menu'>Back to Menu</a> | <a href='/'>Home</a>
        """
    else:
        return "<h1>Item Not Found</h1><p>Sorry, this item doesn't exist.</p><a href='/menu'>Back to Menu</a>", 404

if __name__ == '__main__':
    app.run(debug=True)
