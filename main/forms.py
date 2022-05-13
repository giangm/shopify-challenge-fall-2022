from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Optional

class AddForm(FlaskForm):
    """
    Used to create Add Item form
    """

    # String input field for item name
    item_name = StringField("Item Name", validators=[DataRequired()])
    # Integer input field for item quantity
    item_quantity = IntegerField("Item Quantity", validators=[DataRequired()])
    # Form submit button
    submit = SubmitField("Add item")


class EditForm(FlaskForm):
    """
    Used to create Edit Item form
    """
    
    # String input field for item name
    item_name = StringField("Item Name", validators=[DataRequired()])
    # Integer input field for item quantity
    item_quantity = IntegerField("Item Quantity", validators=[DataRequired()])
    # Form submit button
    submit = SubmitField("Edit item")


class DeleteForm(FlaskForm):
    """
    Used to create Delete Item form
    """
    # String input field for item name
    item_name = StringField("Item Name", validators=[DataRequired()])
    # String input field for comments
    comments = TextAreaField("Comments", validators=[Optional()])
    # Form submit button
    submit = SubmitField("Delete item")