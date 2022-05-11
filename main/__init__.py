import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

## Create Flask instance
app = Flask(__name__)

## Apply configurations based on FLASK_ENV
if app.config["ENV"] == "production":
    app.config.from_object("config.Production")
else:
    app.config.from_object("config.Development")

## Create SQLAlchemy object
db = SQLAlchemy(app)

## Logging configs
logging.basicConfig(filename="app.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")

from main import views