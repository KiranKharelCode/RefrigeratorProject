from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Delete, delete,update
from main import app


db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food_database.db"
db.init_app(app)

class Foods(db.Model):
    __tablename__ = "My_Food"
    id = db.Column(db.INTEGER,nullable=False, primary_key=True)
    name = db.Column(db.String(250),nullable=False)
    quantity = db.Column(db.INTEGER,nullable=False)
    date_added = db.Column(db.String(250),nullable=False)

with app.app_context():
    db.create_all()
