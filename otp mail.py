#import os
import math
import random
import smtplib

#defining the function for generating
#and sending otp
def otp():
  digits="0123456789"
  OTP=""
  for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
  otp = OTP + " is your OTP"
  msg= otp

  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("aishrudrawar@gmail.com", "flblzqroxobldqhq")
  emailid = input("Enter your email: ")
  s.sendmail('&&&&&&&&&&&',emailid,msg)
  a = input("Enter Your OTP >>: ")
  if a == OTP:
    print("Verified")
  else:
    print("Please Check your OTP again")

d=input("if you want to continue type yes else type stop")
print("type stop if you want to stop the program")
if d!="stop":
  otp()
else:
  print("thank you")
  