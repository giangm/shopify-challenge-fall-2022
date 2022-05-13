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
    
    def __repr__(self):
        return f"ID: {self.id}, Item Name: {self.item_name}, Item Quantity: {self.item_quantity}"
    
class DeletedItems(db.Model):
    """
    Database table called DeleteItems, stores items that users want to delete. User needs to confirm that they want to delete
    """
    # Integer column for primary key, ID
    id = db.Column(db.Integer, primary_key=True)
    # Integer foreign key from Inventory table
    item_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))
    # String column for item name
    item_name = db.Column(db.String(100), nullable=False)
    # Quantity column for item quantity
    item_quantity = db.Column(db.Integer, nullable=False)
    # String column for comments
    comments = db.Column(db.String(200))
    
    def __repr__(self):
        return f"ID: {self.id}, Item ID: {self.item_id}, Item Name: {self.item_name}, Item Quantity: {self.item_quantity}, Comments: {self.comments}"