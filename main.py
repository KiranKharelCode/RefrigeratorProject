from flask import Flask,request,redirect,Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os

def send_sms():
    account_sid = os.environ["SID"]
    auth_token = os.environ["TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_=os.environ['FROM_NUMBER'],
    body='This is a test',
    to=os.environ["TO_NUMBER"])


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    print(body)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)