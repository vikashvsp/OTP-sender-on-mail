from email import message
from multiprocessing import context
import smtplib,ssl
import math as m
import random as r
import stdiomask
def OTPgen():
    string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP=""
    varlen=len(string)
    for i in range(6):
        OTP+= string[m.floor(r.random()*varlen)]
    return(OTP)

otp=OTPgen()
#print(otp)
port=465
smtp_server="smtp.gmail.com"
sender_email=input("Enter sender E-mail\n")
print("\n")
print("Enter your password\n")
password=stdiomask.getpass()
print("\n")
receiver_email=input("Enter receiver E-mail\n")
print("\n")

message=f"""
    
    Your OTP is {otp}
    
    """

context=ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)

print("OTP Sent")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
while(True):
    otprcvd=input("Enter the otp you received\n")

    if(otp==otprcvd):
        print("OTP is Correct\n")
        break
    else:
        print("You entered wrong OTP\nPlease enter again:")