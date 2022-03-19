from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    Model in charge of User abstraction storage.
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    # Foreign key to Address
    # address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
    #     nullable=False)
    # address = db.relationship('Address',
    #     backref=db.backref('users', lazy=True))
    phone = db.Column(db.String, nullable=False)
    website = db.Column(db.String, nullable=False)
    # Foreign key to Company
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'),
        nullable=False)
    # company_name = db.Column(db.Integer, db.ForeignKey('company.name'),
    #     nullable=False)
    # company = db.relationship('Company',
    #     backref=db.backref('users', lazy=True))

class Address(db.Model):
    """
    Model in charge of the user's adsress abstraction storage.
    """
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String, nullable=False)
    suite = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.String, nullable=False)    
    #geo = tupla

class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=False)
    catch_phrase = db.Column(db.String, nullable=False)
    bs = db.Column(db.String, nullable=False)
    users = db.relationship('User', backref='company', lazy=True)