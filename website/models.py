from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Intiger, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)