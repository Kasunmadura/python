#!/usr/bin/python
'''
This you can use for send mail attachement 
support python 2.X
Kasun Rathnayaka
Web:http://kasunmadura.com
twitter:kasunmaduraR

'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
#From mail address
fromaddressr = "kasun***@gmail.com"
#To mail address
toaddress = "tomail@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddressr
msg['To'] = toaddress
## mail Subject 
msg['Subject'] = "2nd mail"
 
#put body content here 
body = "THis is second one with attchment"
 
msg.attach(MIMEText(body, 'plain'))
 
##File name 
filename = "my.txt"
###Attachement Location
attachment = open("/home/kasunr/my.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#set you mail password
server.login(fromaddressr,"*************")
text = msg.as_string()
server.sendmail(fromaddressr, toaddress, text)
server.quit()
