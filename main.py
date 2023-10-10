from flask import Flask, request, redirect, Response, render_template, url_for
from wtforms import Form, StringField, validators
from datetime import date
import os


class FoodDataForm(Form):
    pass



def order_data(data):
    today = date.today()
    with open ("FoodData.txt","a") as file:
        for items in data:
            items.append(f'DateAdded: {today}')
            file.write(f'{str(items)} ')
            file.write("\n")



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['KEY']

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("HomePage.html")




@app.route("/add", methods=['GET', 'POST'])
def add_items():
    food_list = []
    form = FoodDataForm()
    if request.method == "POST":
        for items,value in zip(request.form.getlist('food_input'),request.form.getlist('quantity_input')):
            food_list.append([items,value])
        order_data(food_list)
        return redirect(url_for('home'))


    return render_template('Add_Items.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)