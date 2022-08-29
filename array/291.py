# QID: 291
# 
# Email Validation :
# Given a string S check if is a valid email id based on the following Conditions.
# 1)@ should be present;
# 2)@ & . should not be repeated;
# 3)there should be atleast four characters between @ and .;
# 4)there should be at-least 3 characters before @ ;
# 5)the end of mail id should be .com;
# If its a valid email id print 'yes' else print 'no'.
# Input Size : |S| <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# test@gmail.com
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


import re
email = input()
reges = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-][A-Za-z0-9.-][A-Za-z0-9.-][A-Za-z0-9.-][A-Za-z0-9.-]\.[A-Z|a-z]{2,}\b'
if not re.search(reges,email):
  print("no")
else:
  print("yes")