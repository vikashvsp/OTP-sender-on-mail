from email import message
from multiprocessing import context
import smtplib,ssl
port=465
smtp_server="smtp.gmail.com"
sender_email="vspecial85@gmail.com"
receiver_email='vkvikashkumar987@gmail.com'
password=input("type your password")
var=89
message=f"""
    
    This message is {var}automated ;)"""

context=ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)