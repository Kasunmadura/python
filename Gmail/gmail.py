#!/usr/bin/python
'''
This use for send mail using python script 
support python 2.X
Kasun Rathnayaka
Web:http://kasunmadura.com
twitter:kasunmaduraR

'''
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddress = "kasunmaduraeng@gmail.com"
toaddress = "suhada.fernando@pearson.com"
msg = MIMEMultipart()
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = "HI broz"
 
body = "Enter you Massgae"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddress, "Mylovesamu141@#.!")
text = msg.as_string()
server.sendmail(fromaddress, toaddress, text)
server.quit()
