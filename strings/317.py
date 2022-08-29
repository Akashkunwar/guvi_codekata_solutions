# QID: 317
# 
# Given a sentence S.check whether it is in camelcase.print 'yes' if it is in camelcase otherwise print 'no'. 
# input size : |s| <= 100000
# 
# 
# Sample Testcase :
# INPUT
# CodekataChallenge
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = input()
if a[1:].islower():
  print("no")
else:
  print("yes")