from unicodedata import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app=app)


# def create_app():
#     #app.config.from_object(Config)
#     print('Setting environment variables.')
#     #initialize db
#     #db.create_all()
#     # from flaskblog.users.routes import users
#     # from flaskblog.posts.routes import posts
#     # from flaskblog.main.routes import main
#     # from flaskblog.errors.handlers import errors
#     # app.register_blueprint(users)
#     # app.register_blueprint(posts)
#     # app.register_blueprint(main)
#     # app.register_blueprint(errors)
#     return app

# if name=='__main__':
#     create_app()