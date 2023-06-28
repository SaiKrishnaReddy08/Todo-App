from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo_data.db'
app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

from todo_app import routes
from todo_app import models