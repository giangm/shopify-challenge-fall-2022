from main import db

class Inventory(db.Model):
    """
    Database table called Inventory, used to store items
    """
    # Integer column for primary key, ID
    id = db.Column(db.Integer, primary_key=True)
    # Integer foreign key from Inventory table
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'))
    # String column for item name
    item_name = db.Column(db.String(100), nullable=False)
    # Quantity column for item quantity
    item_quantity = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"ID: {self.id}, Foreign Key: {self.warehouse_id}, Item Name: {self.item_name}, Item Quantity: {self.item_quantity}"
    
    
class Warehouse(db.Model):
    """
    Database table called Warehouse, Inventories are assigned to different Warehouses
    """
    # Integer column for primary key, ID
    id = db.Column(db.Integer, primary_key=True)
    # String column for warehouse name
    warehouse_name = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"ID: {self.id}, Warehouse Name: {self.warehouse_name}"
    