# importing the client from the twilio
from twilio.rest import Client
from datetime import *
from time import *

# Your Account Sid and Auth Token from twilio account
account_sid = ""
auth_token = ""
# instantiating the Client
client = Client(account_sid, auth_token)

while ((datetime.now().hour)<=18):
    # sending message
    message = message = client.messages.create(
        body="", from_="", to=""
    )
    # printing the sid after success
    print(message.sid)
    sleep(30)