#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In Gmail in Security set "Less secure app access".

$ ebook-convert Pocket.recipe .mobi && ./Pocket-send-to-amazon.py

"""


import smtplib
import socket
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from base64 import encodebytes

FROM = 'YOUR APPROVED MAIL WITH AMAZON'
TO = 'YOUR MAIL TO SEND TO AMAZON@KINDLE.COM'
LOGIN = 'LOGIN'
PASSWORD = 'PASSWORD'

def send_email():
    msg = MIMEMultipart()
    msg['Subject'] = 'test'
    msg['From'] = FROM
    msg['To'] = TO
    body = "This is an email with attachment sent from Python"
    msg.attach(MIMEText(body, "plain"))
    filename = "Pocket.mobi"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    msg.attach(part)
    text = msg.as_string()
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(LOGIN, PASSWORD)
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print('OK')
    except smtplib.SMTPRecipientsRefused:
        print("smtplib.SMTPRecipientsRefused")
        return 1
    except socket.error:
        print('Error sending: socket.error: [Errno 110] Connection timed out')
        return 1

if __name__ == '__main__':
    send_email()
