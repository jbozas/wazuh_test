from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    Model in charge of User abstraction storage.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    # Foreign key to Address
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
                           nullable=False)
    address = db.relationship('Address',
                              backref=db.backref('users_address', lazy=True))
    phone = db.Column(db.String, nullable=False)
    website = db.Column(db.String, nullable=False)
    # Foreign key to Company
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'),
                           nullable=False)
    company = db.relationship('Company',
                              backref=db.backref('users_company', lazy=True))

    @property
    def serialize(self) -> dict:
        """
        Serialize User object to use in API response.
        This should be a Serializer instead.
        """
        return {
            'company': self.company.serialize,
            'website': self.website,
            'phone': self.phone,
            'address': self.address.serialize,
            'email': self.email,
            'username': self.username,
            'name': self.name,
            'id': self.id,
        }

    def retrieve_tasks(self, filters) -> dict:
        """
        Returns a dict including all the user Tasks.
        """
        filters = filters.to_dict()
        filters['user_id'] = self.id
        return Task.query.filter_by(**filters).all()


class Address(db.Model):
    """
    Model in charge of the user's adsress abstraction storage.
    """
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String, nullable=False)
    suite = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.String, nullable=False)

    @property
    def serialize(self) -> dict:
        """
        Serialize Address object to use in API response.
        This should be a Serializer instead.
        """
        return {
            'zipcode': self.zipcode,
            'city': self.city,
            'suite': self.suite,
            'street': self.street,
        }


class Company(db.Model):
    """
    Abstraction to user's companies.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=False)
    catch_phrase = db.Column(db.Text, nullable=False)
    bs = db.Column(db.String, nullable=False)

    @property
    def serialize(self) -> dict:
        """
        Serialize Company object to use in API response.
        This should be a Serializer instead.
        """
        return {
            'bs': self.bs,
            'catch_phrase': self.catch_phrase,
            'name': self.name,
        }


class Task(db.Model):
    """
    Model in charge of Transaction Task abstraction.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    user = db.relationship('User',
                           backref=db.backref('tasks', lazy=True))

    @property
    def serialize(self) -> dict:
        """
        Serialize Task object to use in API response.
        This should be a Serializer instead.
        """
        return {
            'completed': self.completed,
            'title': self.title,
            'user_id': self.user_id,
        }
