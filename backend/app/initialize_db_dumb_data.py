import json
from flask_sqlalchemy import SQLAlchemy
from models import Company, Address, User
from flask import Flask
from config import Config

def main():
    f = open("user/data/users.json")
    data = json.load(f)
    for user  in data:
        # Create the company
        company = Company(
                name=user['company']['name'],
                catch_phrase=user['company']['catchPhrase'],
                bs=user['company']['bs']
            )
        # address = Address(
        #     street=user['address']['street'],
        #     suite=user['address']['suite'],
        #     city=user['address']['city'],
        #     zipcode=user['address']['zipcode'],
        # )
        user = User(
            id=user['id'],
            name=user['name'],
            username=user['username'],
            email=user['email'],
            #address=address,
            phone=user['phone'],
            website=user['website'],
            company=company,
        )
        db.session.add(company)
        db.session.add(user)
    db.session.commit()          
            


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy()
    db.init_app(app)
    db.create_all(app=app)
    with app.app_context():
        main()