from main import app
from flask import Blueprint, request, render_template

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(404)
def error_404(e):
    """
    Custom 404 page not found error page
    """

    ## Log page not found event
    app.logger.error(f"404 - {request.path} Page Not Found", "error")
    return render_template("errors/404.html"), 404


@errors.app_errorhandler(500)
def error_500(e):
    """
    Custom 500 internal server error page
    """

    ## Log page not found event
    app.logger.error(f"500 - {request.path} Internal Server Error", "error")
    return render_template("errors/500.html"), 500