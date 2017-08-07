#!/usr/bin/python
from smtplib import SMTP
import smtplib

smtp = SMTP()
smtp.set_debuglevel(2)
smtp.connect('YOUR.MAIL.SERVER', 26)
smtp.login('USERNAME@DOMAIN', 'PASSWORD')



sender = 'arpank200@gmail.com'
receivers = ['arpank200@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except   :
   print ("Error: unable to send email")