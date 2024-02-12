import pandas as pd
import datetime as dt
import random as rd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl



SENDER=""
PW=""


smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender_password = PW
context = ssl.create_default_context()



today=(dt.datetime.now().month,dt.datetime.now().day)

data=pd.read_csv("birthdays.csv")

birthdays={(dr["month"],dr["day"]):dr for idx,dr in data.iterrows()}

if today in birthdays:
    person=birthdays[today]
    file_path=f"letter{rd.randint(1,2)}.txt"
    with open(file_path) as file:
        contents=file.read()
        contents=contents.replace("[NAME]", person["name"])
    msg = MIMEMultipart()
    msg['From'] = SENDER
    msg['To'] = person["email"]
    msg['Subject'] = 'Happy Birthday'
    body = contents
    msg.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(SENDER, sender_password)
        server.sendmail(SENDER, person["email"], msg.as_string())