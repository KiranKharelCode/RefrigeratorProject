import time
from BingAI import food_Query,answer
from flask import Flask, request, redirect, Response, render_template, url_for,flash
from wtforms import Form, StringField, validators
from datetime import date
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Delete, delete,update
import json
from datetime import date, datetime



class FoodDataForm(Form):
    pass

class FoodSearchForm(Form):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']



db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food_database.db"
db.init_app(app)

class Foods(db.Model):
    __tablename__ = "My_Food"
    id = db.Column(db.INTEGER,nullable=False, primary_key=True)
    name = db.Column(db.String(15),nullable=False)
    quantity = db.Column(db.INTEGER,nullable=False)
    expire_date = db.Column(db.String(15), nullable=False)
    date_added = db.Column(db.String(15),nullable=False)
    bing_data = db.Column(db.String(15),nullable=False)


with app.app_context():
    db.create_all()

def time_calc():
    def numOfDays(date1, date2):
        if date2 > date1:
            return (date2 - date1).days
        else:
            return (date1 - date2).days

    date_str = ''
    date_object = datetime.strptime(date_str, '%Y-%m-%d').date()

    date1 = date(date_object.year, date_object.month, date_object.day)
    date2 = date('')
    print(numOfDays(date1, date2), "days")
def order_collected_data(data):
    food_str = f'{data}'
    food_str = food_str.replace('“', '"')
    food_str = food_str.replace('”', '"')
    json_object = json.loads(food_str)
    json_object = [(key.upper(), value) for key, value in json_object.items()]
    return json_object


def order_data(form):
    with app.app_context():
        Question_list = []
        food_items = []

        for items,value,expdate in zip(request.form.getlist('food_input'),request.form.getlist('quantity_input'),request.form.getlist('expire_input')):
            food_items.append((items.upper(),value,expdate))
            Question_list.append(f"Answer the question in 2 words or less: 'How long can {items} stay in the fridge' without sourcing anything")
        question = " ".join(Question_list)
        returned_data = order_collected_data(food_Query(question + ' Answer for each questions in 2 words or less and nothing more, i dont want a json answer, and answer in this format "{"item":time,}"',len(food_items)+2))

        for items in range (0,len(food_items)):
            new_food_items = Foods(name=food_items[items][0], quantity=food_items[items][1], expire_date = food_items[items][2], date_added=date.today(),bing_data=returned_data[items][1])
            db.session.add(new_food_items)
            db.session.commit()





@app.route("/", methods=['GET','POST'])
def home():
    form = FoodSearchForm()
    db_foods = Foods.query.all()

    return render_template("HomePage.html",foods = db_foods,form=form)




@app.route("/<id>",methods=['GET','POST'])
def delete_items(id):

    with app.app_context():
        food_delete = db.session.execute(db.select(Foods).where(Foods.id == id)).scalar()
        if food_delete is not None:
            db.session.delete(food_delete)
            db.session.commit()
        else:
            pass
 
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