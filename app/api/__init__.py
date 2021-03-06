from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb------"

mongodb_client = PyMongo(app)
db = mongodb_client.db

from api import routes