from flask import Flask,request,redirect,Response,render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os

def send_sms(sent_sms):
    account_sid = os.environ["SID"]
    auth_token = os.environ["TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_=os.environ['FROM_NUMBER'],
    body=f"{sent_sms}",
    to=os.environ["TO_NUMBER"])


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    if "hello" in str(body):
        send_sms("Hello detected")
    else:
        pass

    return render_template('Data.html')


if __name__ == "__main__":
    app.run(debug=True)