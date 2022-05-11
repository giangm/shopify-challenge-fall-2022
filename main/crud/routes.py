from main import app, db
from flask import Blueprint, request, redirect, url_for, flash
from main.models import Inventory

crud = Blueprint("crud", __name__)

@crud.route("/add", methods=["POST"])
def add():
    """
    Adds new row (item) or updates existing row (item) in inventory
    """

    try:
        ## Get request parameters
        item_name = request.form["item_name"].strip()
        item_quantity = int(request.form["item_quantity"].strip())

        ## Check if inputs/parameters are empty
        if item_name is None or item_quantity is None or item_name == "" or item_quantity == "":
            ## Log empty input/parameter event
            app.logger.error("Input(s) or request parameter(s) is empty")
            ## Send client alert
            flash("Input(s) cannot empty", "error")
            return redirect(url_for("index"))

        ## Check invalid quantity
        if item_quantity <= 0:
            ## Log invalid quantity event
            app.logger.error("Quantity lower than 1")
            ## Send client alert
            flash("Quantity cannot be lower than 1", "error")
            return redirect(url_for("index"))

        ## Check for existing row in product table
        item = Inventory.query.filter_by(item_name=item_name).first()

        if item is None:
            ## Insert new row
            item = Inventory(item_name=item_name, item_quantity=item_quantity)
            db.session.add(item)
            ## Log event
            app.logger.info(f"Inserted {item}")

        else:
            ## Update existing row
            item.item_quantity += item_quantity
            ## Log event
            app.logger.info(f"Updated {item}")

        ## Commit transaction
        db.session.commit()
    
    except ValueError:
        ## Log event
        app.logger.error("Invalid value(s)")
        ## Send client alert
        flash("Invalid value(s), try again")
        return redirect(url_for("index"))

    ## Send client alert
    flash("Added item successfully", "info")
    return redirect(url_for("index"))


@crud.route("/edit", methods=["POST"])
def edit_item():
    """
    Edits quantity of existing row (item) in inventory
    """

    try:
        ## Get request parameters
        item_name = request.form["item_name"].strip()
        item_quantity = int(request.form["item_quantity"].strip())

        ## Check if inputs/parameters are empty
        if item_name is None or item_quantity is None or item_name == "" or item_quantity == "":
            ## Log empty input/parameter event
            app.logger.error("Input(s) or request parameter(s) is empty")
            ## Send client alert
            flash("Input(s) cannot empty", "error")
            return redirect(url_for("index"))

        ## Check invalid quantity
        if item_quantity <= 0:
            ## Log invalid quantity event
            app.logger.error("Quantity lower than 1")
            ## Send client alert
            flash("Quantity cannot be lower than 1", "error")
            return redirect(url_for("index"))

        ## Check for existing row
        item = Inventory.query.filter_by(item_name=item_name).first()

        if item is None:
            ## Log attempt to update non-existing row (item) event
            app.logger.error("Attempt to update row that does not exists")
            ## Send client alert
            flash("Item does not exist", "error")

        else:
            ## Update the row
            item.item_quantity = item_quantity
            db.session.commit()
            ## Log udpated row (item) event
            app.logger.info(f"Updated {item}")
            ## Send client alert
            flash("Item updated successfully", "info")

    except ValueError:
        ## Log invalid value event
        app.logger.error("Invalid value(s)")
        ## Send client alert
        flash("Invalid value(s), try again")
        return redirect(url_for("index"))

    return redirect(url_for("index"))


@crud.route("/delete", methods=["POST"])
def delete():
    """
    Delete existing row (item) from inventory
    """

    ## Get request parameters
    item_name = request.form["item_name"].strip()

    ## Check if input/parameter is empty
    if item_name is None  or item_name == "":
        ## Log empty input/paremeter event
        app.logger.error("Input or request parameter is empty")
        ## Send client alert
        flash("Input cannot empty", "error")
        return redirect(url_for("index"))

    ## Check if row exists
    item = Inventory.query.filter_by(item_name=item_name).first()

    if item is None:
        ## Log attempt to delete non-existing row (item) event
        app.logger.error("Attempt to delete non-existing item")
        ## Send client alert
        flash("Input cannot empty", "error")
        return redirect(url_for("index"))

    else:
        ## Delete row
        db.session.delete(item)
        db.session.commit()
        ## Log delete row (item) event
        app.logger.info(f"Deleted {item}")

    ## Send client alert
    flash("Item deleted successfully", "info")
    return redirect(url_for("index"))
