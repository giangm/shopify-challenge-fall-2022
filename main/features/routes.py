from main import app, db
from flask import Blueprint, request, flash, redirect, url_for
from main.models import Inventory, DeletedItems

features = Blueprint("features", __name__)

@features.route("/confirm_deletion", methods=["POST"])
def confirm_deletion():
    """
    Confirm that item can be deleted from deleteitems table
    """
    
    # Get request parameters
    item_ids = request.form.getlist("items")
    
    
    for id in item_ids:
        # Check if row exists
        item = DeletedItems.query.filter_by(item_id=id).first()
    
        # Check which type of button was clicked
        if request.form["button"] == "Confirm Delete":
            if item is None:
                # Log attempt to access non-existing item
                app.logger.error("Attempt to access non-existing item")
                # Send client alert
                flash("Item not found", "error")
                return redirect(url_for("index"))
            
        elif request.form["button"] == "Undelete Item(s)":
            
            # Check if item is already in inventory
            item_in_inventory = Inventory.query.filter_by(item_name=item.item_name).first()

            if item_in_inventory is None:
                # Re-insert item into inventory table
                i = Inventory(id=item.item_id, item_name=item.item_name, item_quantity=item.item_quantity)
                db.session.add(i)
                app.logger.info(f"Inserted {i}")
                
            else:
                # Update existing row
                item_in_inventory.item_quantity += item.item_quantity
                # Log event
                app.logger.info(f"Updated {item_in_inventory}")

        # Delete row
        db.session.delete(item)

        # Commit transaction
        db.session.commit()
        
    return redirect(url_for("index"))
    
    