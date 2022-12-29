import math
import random
import re
import smtplib
import time


# Define a function for
# for validating an Email
def validEmail(s):
    pattern = r'^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.match(pattern,s):
        return True
    else:
        return False

#define a function to generate OTP 
def generateOTP():
  digits="0123456789"
  OTP=""
  for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
  otp = OTP + " is your OTP"
  msg=otp
  global y
  y=OTP 
  return OTP

#This function is to send the OTP 
#if the given email id is valid
#by using validEmail function 
def sendOTP():
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("aishrudrawar@gmail.com", "flblzqroxobldqhq")
  emailid = input("Enter your email: ")
  if validEmail(emailid):
    global x
    x=generateOTP()    
    s.sendmail('&&&&&&&&&&&',emailid, x, "IS YOUR OTP")
  return x


#This function will take the OTP from user
#cross check it with the OTP we sned
#and validate the OTP 
def validOTP():
  z=(sendOTP())
  print(time.time())
  print("enter your OTP:")
  while (time.time()-start_time<20):
    print(time.time()-start_time)
    yourotp = int(input())  
    if (int(z) == int(yourotp)):
      print("Verified")
    else:
      print("Please Check your OTP again")
      continue 
  else:
    print("your time limit exceeded",time.time()-start_time)

# Driver Code
if __name__ == '__main__':
    start_time = time.time()
    print(start_time)
    d=input("if you want to continue type yes else type stop")
    if d!="stop":
      validOTP()
    else:
      print("thank you")
        