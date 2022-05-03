from cgitb import html
from email import message
from multiprocessing import context
import smtplib,ssl
import math as m
import random as r
import stdiomask
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def OTPgen():
    string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP=""
    varlen=len(string)
    for i in range(6):
        OTP+= string[m.floor(r.random()*varlen)]
    return(OTP)

otp=OTPgen()
port=465
smtp_server="smtp.gmail.com"
sender_email=input("Enter sender E-mail\n")
print("\n")
print("Enter your password\n")
password=stdiomask.getpass()
print("\n")
receiver_email=input("Enter receiver E-mail\n")
print("\n")

message=MIMEMultipart("alternative")
message["Subject"]="OTP Mailer"
message["From"]=sender_email
message["To"]=receiver_email

text="""\

"""

html=f"""\
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>mail</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
</head>

<body>
    <nav class="navbar navbar-light bg-light">
        <div class="container-fluid">
            <div class="navbar-brand" href="#">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Otp_bank_Logo_old.svg/778px-Otp_bank_Logo_old.svg.png"
                    alt="" width="30" height="24" class="d-inline-block align-text-top" />
                OTP GENERATOR
            </div>
        </div>
    </nav>
    <div class="alert alert-success" role="alert">Your OTP is :-
        <button type="button" id="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Your OTP">
            {otp}
        </button>
    </div>
    

</body>

</html>
"""
part1=MIMEText(text,"plain")
part2=MIMEText(html,"html")

message.attach(part1)
message.attach(part2)

context=ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())

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