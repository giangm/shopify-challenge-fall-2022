from main import db

class Inventory(db.Model):
    """
    Database table called Inventory, used to store items
    """
    # Integer column for primary key, ID
    id = db.Column(db.Integer, primary_key=True)
    # String column for item name
    item_name = db.Column(db.String(100), nullable=False)
    # Quantity column for item quantity
    item_quantity = db.Column(db.Integer, nullable=False)
    
    def __init__(self, id, item_name, item_quantity):
        self.id = id
        self.item_name = item_name
        self.item_quantity = item_quantity
        
    def __repr__(self):
        return f"ID: {self.id}, Item Name: {self.item_name}, Item Quantity: {self.item_quantity}"