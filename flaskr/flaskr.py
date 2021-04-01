import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_gridify import FlaskGridify
from flask_table import Table, Col
import sqlite3
from app import app as application

# Get some objects
# class Item(object):
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description


# def create_app(test_config=None):
    # create and configure the app
    #conn = sqlite3.connect("test.db")

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'test.db'),
)

db = SQLAlchemy(app)
 

#with app.test_request_context('/git'):
#    resp = app.process_response(resp)



# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass
 

from flaskr import routes