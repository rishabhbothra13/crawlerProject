import smtplib
import os
import scrawlerdb
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart('alternative')
user = 'rishabhbothra13@gmail.com'  
passw='baarbaarbhuljatahoon'
sender='rishabhbothra13@gmail.com'
receiver=['rishabhbothra13@gmail.com']


part=MIMEText(scrawlerdb.message.encode('utf-8'),'html')
msg.attach(part)
try:
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(user,passw)
    server.sendmail(sender,receiver,msg.as_string())
    server.close()
    print "mail sent"
except Exception as e:
    print e
