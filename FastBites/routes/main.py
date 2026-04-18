from flask import Blueprint, abort
from data import menu_items, get_item_by_id

# Create a Blueprint for main routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """Home page route"""
    return '''
    <h1>Welcome to FastBites!</h1>
    <p>Your favorite food delivery service</p>
    <ul>
        <li><a href="/menu">View Full Menu</a></li>
    </ul>
    '''

@main_bp.route('/menu')
def menu():
    """Menu page route - displays all available food items"""
    html = '<h1>Our Menu</h1><ul>'
    for item in menu_items:
        html += f'<li><a href="/item/{item["id"]}">{item["name"]} - ${item["price"]}</a></li>'
    html += '</ul><br><a href="/">Back to Home</a>'
    return html

@main_bp.route('/item/<int:item_id>')
def item_detail(item_id):
    """Specific item page route - shows details for a single menu item"""
    item = get_item_by_id(item_id)
    
    if item is None:
        abort(404)
    
    return f'''
    <h1>{item['name']}</h1>
    <p><strong>Price:</strong> ${item['price']}</p>
    <p>{item['description']}</p>
    <br>
    <a href="/menu">Back to Menu</a> | <a href="/">Home</a>
    '''

@main_bp.errorhandler(404)
def not_found_error(error):
    """Custom 404 error handler"""
    return '''
    <h1>404 - Item Not Found</h1>
    <p>Sorry, that food item does not exist.</p>
    <a href="/menu">Return to Menu</a>
    ''', 404
