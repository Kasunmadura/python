#!/usr/bin/python
'''
This use for send mail using python script 
support python 2.X
Kasun Rathnayaka
Web:http://kasunmadura.com
twitter:kasunmaduraR

Please change FROM and TO mail address and PASSWORD 

And also change your SUBJECT and body

'''
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddress = "FROM mail"
toaddress = "TO MAIL"
msg = MIMEMultipart()
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = "HI broz"
 
body = "Enter you Massgae"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddress, "PASSWORD")
text = msg.as_string()
server.sendmail(fromaddress, toaddress, text)
server.quit()
