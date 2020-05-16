#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
In Gmail in Security set "Less secure app access".

(py37) [mx] Pocket-Plus-Calibre-Plugin$ git:(master) ✗ rm Pocket.mobi; ebook-convert Pocket.recipe .mobi && ./Pocket-send-to-amazon.py
Conversion options changed from defaults:
  test: None
1% Converting input to HTML...
InputFormatPlugin: Recipe Input running
Using custom recipe
Using user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
1% Fetching feeds...
1% Got feeds from index page
1% Trying to download cover...
1% Generating masthead...
Synthesizing mastheadImage
1% Starting download [5 threads]...
17% Article downloaded: Sending an email via the Python email library throws error "expected string or bytes-like object"
34% Article downloaded: How to Get Free Magazines on Your Kindle with Calibre
Failed to generate default cover
34% Feeds downloaded to /private/var/folders/yc/ssr9692s5fzf7k165grnhpk80000gp/C/calibre_4.16.0_tmp_fXeFHz/HvTO4__plumber/index.html
34% Download finished
Parsing all content...
Forcing feed_0/article_0/index.html into XHTML namespace
Forcing feed_1/article_0/index.html into XHTML namespace
Forcing index.html into XHTML namespace
Referenced file u'feed_2/index.html' not found
34% Running transforms on e-book...
Merging user specified metadata...
Detecting structure...
Flattening CSS and remapping font sizes...
Source base font size is 12.00000pt
Removing fake margins...
Cleaning up manifest...
Trimming unused files from manifest...
Creating MOBI Output...
67% Running MOBI Output plugin
Serializing resources...
Converting TOC for MOBI periodical indexing...
Creating MOBI 6 output
Generating in-line TOC...
Applying case-transforming CSS...
Rasterizing SVG images...
Converting XHTML to Mobipocket markup...
Serializing markup content...
  Compressing markup content...
Generating MOBI index for a periodical
MOBI output written to /Users/magnus/workspace/Pocket-Plus-Calibre-Plugin/Pocket.mobi
Output saved to   /Users/magnus/workspace/Pocket-Plus-Calibre-Plugin/Pocket.mobi
OK
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
        server.sendmail(FROM, TO, text)
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
