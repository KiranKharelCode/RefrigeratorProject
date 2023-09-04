from flask import Flask,request,redirect,Response,render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from wtforms import Form, StringField, validators
from datetime import date
import os


class FoodDataForm(Form):
    pass

def send_sms(sent_sms):
    account_sid = os.environ["SID"]
    auth_token = os.environ["TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_=os.environ['FROM_NUMBER'],
    body=f"{sent_sms}",
    to=os.environ["TO_NUMBER"])
    return render_template('Message.html',message=f'{sent_sms}')

def order_data(data):
    today = date.today()
    with open ("FoodData.txt","a") as file:
        for items in data:
            items.append(f'DateAdded: {today}')
            file.write(f'{str(items)} ')
            file.write("\n")



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['KEY']

@app.route('/sms',methods=['GET','POST'])
def sms_reply():
    body = request.values.get('Body', None)
    if "hello" in str(body):
        return send_sms("Hello detected")

    return render_template("Message.html",message="Message sent")

@app.route("/add", methods=['GET', 'POST'])
def add_items():
    food_list = []
    form = FoodDataForm()
    if request.method == "POST":
        for items,value in zip(request.form.getlist('food_input'),request.form.getlist('quantity_input')):
            food_list.append([items,value])
        order_data(food_list)


    return render_template('Data.html',form=form)


if __name__ == "__main__":
    app.run(debug=True)