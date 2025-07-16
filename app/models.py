# models.py
# Define your database models here


from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class DJ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone_no = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    mixes = db.relationship('Mix', backref='dj', lazy=True)

    def __repr__(self):
        return f'<DJ {self.username}>'



class Mix(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    date_uploaded = db.Column(db.DateTime, nullable=False)
    stream = db.Column(db.Integer, default=0)
    downloads = db.Column(db.Integer, default=0)
    dj_id = db.Column(db.Integer, db.ForeignKey('DJ.id'), nullable=False)
    file_path = db.Column(db.String(255))  # Stores the uploaded mix file path

    def __repr__(self):
        return f'<Mix {self.name}>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
