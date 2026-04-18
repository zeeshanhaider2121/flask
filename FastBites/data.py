# In-memory data storage for menu items
menu_items = [
    {'id': 1, 'name': 'Margherita Pizza', 'price': 12.99, 'description': 'Classic pizza with tomato sauce and mozzarella', 'image': 'pizza.jpg'},
    {'id': 2, 'name': 'Chicken Burger', 'price': 8.99, 'description': 'Grilled chicken with lettuce and mayo', 'image': 'burger.jpg'},
    {'id': 3, 'name': 'Caesar Salad', 'price': 7.99, 'description': 'Fresh romaine lettuce with caesar dressing', 'image': 'salad.jpg'}
]

def get_item_by_id(item_id):
    """Helper function to get a menu item by its ID"""
    for item in menu_items:
        if item['id'] == item_id:
            return item
    return None
