from main import app
from main.forms import *
from flask import render_template

from main.models import Inventory, DeletedItems

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Index/Home page of web application
    """
    
    # Query all items from inventory table
    items = Inventory.query.order_by(Inventory.id)
    # Query all items from deleteitems table
    deleted_items = DeletedItems.query.order_by(DeletedItems.id)
    return render_template("index.html", items=items, deleted_items=deleted_items, forms=[AddForm(), EditForm(), DeleteForm()])