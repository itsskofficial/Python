import requests
import geocoder
from datetime import datetime
from smtplib import *

ip=geocoder.ip('me')
location=ip.latlng
MY_LAT = location[0] # Your latitude
MY_LONG = location[1] # Your longitude
MY_EMAIL = "abc@gmail.com"
MY_PASS = "abcd1234"
YOUR_EMAIL = "xyz@gmail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if abs(iss_latitude-MY_LAT)<=5 and time_now.hour>sunset:
    connection=SMTP("smtp.google.com")
    connection.starttls()
    connection.login(user=MY_EMAIL,password=MY_PASS)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs=YOUR_EMAIL,msg="Subject:ISS Tracker\n\nThe ISS is above you. Go out and look up!")




