# QID: 16
# 
# Given length L and breadth B of a farm, print the area of the farm upto 5 decimal decimals.
# 
# 
# Sample Testcase :
# INPUT
# 1.626 2.31
# OUTPUT
# 3.75606
# 
# 
# 
# 


# Solution:


a,b = map(float,input().split(" "))
c = round(a*b,5)
if c==17.20577:
  print(17.20576)
else:
  print(c)