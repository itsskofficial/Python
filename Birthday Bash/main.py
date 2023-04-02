from os import *
from smtplib import *
from random import *
from datetime import *
import smtplib
from pandas import *

today=datetime.now()
dataframe=read_csv("birthdays.csv")
birthdays=dataframe.to_dict("dict")
lines = len(dataframe)

for i in range(0,lines):
    if today.month==birthdays["month"][i]:
        if today.day==birthdays["day"][i]:
            file=choice(listdir("letter_templates"))
            msg=file.replace("[NAME]",birthdays["name"][i])
            connection = SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user="example@gmail.com",password="abcba")
            connection.sendmail(from_addr="example@gmail.com",to_addrs="example@yahoo.com",msg=msg)
            connection.close()
        else:
            continue
    else:
        continue
