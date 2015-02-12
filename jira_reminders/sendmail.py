__author__ = 'talluri'
#!/usr/bin/python

import smtplib

sender = 'srikanteswararao.talluri@citrix.com'
receivers = ['srikanteswararao.talluri@citrix.com']

message = """From: From Person <srikanteswararao.talluri@citrix.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP('https://10.151.60.57/EWS/Exchange.asmx', port=443)
smtpObj.sendmail(sender, receivers, message)
print "Successfully sent email"

