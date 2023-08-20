from twilio.rest import Client
import os

def send_text():
    account_sid = os.environ["SID"]
    auth_token = os.environ["TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_=os.environ['FROM_NUMBER'],
      body='This is a test',
      to=os.environ["TO_NUMBER"]
    )

    print(message.sid)
