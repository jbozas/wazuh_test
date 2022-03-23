import json
from flask_sqlalchemy import SQLAlchemy
from models import Company, Address, User, Task
from flask import Flask
from config import Config


def _load_tasks():
    f = open("user/data/tasks.json")
    data = json.load(f)
    for task in data:
        task = Task(
            id=task['id'],
            title=task['title'],
            completed=task['completed'],
            user_id=task['user_id']
        )
        db.session.add(task)


def _load_users():
    f = open("user/data/users.json")
    data = json.load(f)
    for user in data:
        company = Company(
            name=user['company']['name'],
            catch_phrase=user['company']['catchPhrase'],
            bs=user['company']['bs']
        )
        address = Address(
            street=user['address']['street'],
            suite=user['address']['suite'],
            city=user['address']['city'],
            zipcode=user['address']['zipcode'],
        )
        user = User(
            id=user['id'],
            name=user['name'],
            username=user['username'],
            email=user['email'],
            address=address,
            phone=user['phone'],
            website=user['website'],
            company=company,
        )
        db.session.add(address)
        db.session.add(company)
        db.session.add(user)


def main():
    """
    Takes all json file data and storage it on to database.
    """
    _load_users()
    _load_tasks()
    db.session.commit()


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy()
    db.init_app(app)
    db.create_all(app=app)
    with app.app_context():
        main()


# DUMMY DATA
# company = Company(
#                 name='Dummy name',
#                 catch_phrase='Dummy catch phrase',
#                 bs='Dummy bs'
#             )
# address = Address(
#     street='Dummy address',
#     suite='Dummy suite',
#     city='Dummy city',
#     zipcode='Dummy zipcode',
# )
# user = User(
#     id=1,
#     name='name',
#     username='username',
#     email='email',
#     address=address,
#     phone='phone',
#     website='website',
#     company=company,
# )


# Deleting an object with Flask. This doenst erase in cascade.
# user = db.session.query(User).filter(User.id==1).first()
# db.session.delete(user)
# db.session.commit()
