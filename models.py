from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), unique=False, nullable=False)
    comment = db.Column(db.String(250), unique=False, nullable=False)
