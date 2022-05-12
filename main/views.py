from main import app
from main.forms import *
from flask import render_template, request

from main.models import Inventory

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Index/Home page of web application
    """
    
    # Query all items from database
    items = Inventory.query.order_by(Inventory.id)
    return render_template("index.html", items=items, forms=[AddForm(), EditForm(), DeleteForm()])