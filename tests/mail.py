import string
import time
from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL
from email.MIMEMultipart import MIMEMultipart

import smtplib
msg = MIMEMultipart()
filename = "~/Reports/example_dir/Test_TestOpenWeatherMap_2018-10-12_02-27-28.html"
f = file(filename)
fromaddr = 'poppertester1@gmail.com'
toaddrs  = 'karunakarsapogu@gmail.com '
message = 'test mail and i have added the same code in the attachment as well'

attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment',   filename=filename)
msg.attach(attachment)
username = 'poppertester1'
password = 'poptester1'

# The actual mail send
#server = smtplib.SMTP('smtp.gmail.com:587')
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg.as_string(message) )
server.quit()
