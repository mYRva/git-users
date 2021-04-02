import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_gridify import FlaskGridify
from flask_table import Table, Col
import sqlite3


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'test.db'),
)

db = SQLAlchemy(app)
 
 

from flaskr import routes