import smtplib
from string import *
from NameResolution import *


nr = NameResolution()
toNumber = raw_input("Enter the number of the person you'd like to text: ")
toService = nr.get_server(raw_input("Enter the provider: "))

SERVER = 'smtp.webfaction.com'
PORT=465
FROM = "brandon@brandonrunyon.com"
TO = toNumber+'@'+toService 

message= raw_input("Enter Your message: ")
smtpuser='brandon'
smtppass='jankcb3928'

################################
print 'opening session'
session = smtplib.SMTP_SSL(SERVER,PORT)

session.set_debuglevel(1)

print 'checking login'
session.login(smtpuser,smtppass)
session.sendmail(FROM, TO, message)

session.quit()
