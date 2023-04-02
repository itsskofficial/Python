# importing the client from the twilio
from twilio.rest import Client
from datetime import *
from time import *

# Your Account Sid and Auth Token from twilio account
account_sid = "ACa0989588c68a49c8a2751da99be3c2b1"
auth_token = "b81b3e0f66a7bcff7373113715a40df1"
# instantiating the Client
client = Client(account_sid, auth_token)

while ((datetime.now().hour)<=18):
    # sending message
    message = message = client.messages.create(
        body="E Ojas", from_="+15092535647", to="+918408849900"
    )
    # printing the sid after success
    print(message.sid)
    sleep(30)