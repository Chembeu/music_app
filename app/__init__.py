from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .auth import auth_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change to a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

from . import routes
