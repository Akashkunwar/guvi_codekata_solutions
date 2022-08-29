# QID: 163
# 
# Given an array of numbers and another number k. Find whether K exists and the number of time k repeats. If it does not exist just print no.
# Input Size : |N| <= 1000000
# 
# 
# Sample Testcase :
# INPUT
# 5 3
# 3 3 4 4 7
# OUTPUT
# yes 2
# 
# 
# 
# 


# Solution:


a,b = map(int,input().split())
c = [int(i) for i in input().split(" ")]
if c.count(b)==0:
  print("no")
else:
  print("yes",c.count(b))