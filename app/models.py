from datetime import date

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    modules = db.relationship('Module', back_populates='owner', lazy=True)
    joined = db.Column(db.Date)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.joined = date.today()

    def __repr__(self):
        return f'<id {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


class Module(db.Model):
    __tablename__ = 'modules'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    owner = db.relationship('User', back_populates='modules')
    name = db.Column(db.String(), nullable=False)
    source = db.Column(db.String(), nullable=False)

    def __init__(self, name, source):
        self.name = name
        self.source = source

    def __repr__(self):
        return f'<id {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'source': self.source,
            'owner': self.owner.username,
        }
