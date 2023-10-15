from flask import Flask, request, redirect, Response, render_template, url_for
from wtforms import Form, StringField, validators
from datetime import date
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Delete, delete,update


class FoodDataForm(Form):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['KEY']



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

def order_data(form):
    with app.app_context():
        for items,value in zip(request.form.getlist('food_input'),request.form.getlist('quantity_input')):
            new_food_items = Foods(name=items, quantity=value, date_added=date.today())
            db.session.add(new_food_items)
            db.session.commit()



@app.route("/", methods=['GET','POST'])
def home():
    db_foods = Foods.query.all()
    return render_template("HomePage.html",foods = db_foods)



@app.route("/<id>",methods=['GET','POST'])
def delete_items(id):
    print(id)
    with app.app_context():
        food_delete = db.session.execute(db.select(Foods).where(Foods.id == id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(food_delete)
        db.session.commit()
    return redirect(url_for('home'))
@app.route("/add", methods=['GET', 'POST'])
def add_items():
    form = FoodDataForm()
    if request.method == "POST":
        order_data(form)
        return redirect(url_for('home'))


    return render_template('Add_Items.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)