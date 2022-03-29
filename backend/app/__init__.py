from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
from app.routes import *  # NOQA
db = SQLAlchemy(app=app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
