from application import app
# from app.forms import *
from flask import render_template

# from app.models import Inventory

@app.route("/")
def index():
    """
    Index/Home page of web application
    """

    ## Query all items from database
    # items = Inventory.query.order_by(Inventory.id)
    # return render_template("index.html", items=items, forms=[AddForm(), EditForm(), DeleteForm(), ExportForm()])
    return "hiu"