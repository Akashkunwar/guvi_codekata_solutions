# QID: 198
# 
# Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.
# Input Size : A,B,C <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 3 4 5
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b,c = map(int, input().split(" "))
if (a!=b and b!=c and c!=a):
  print("yes")
else:
  print("no")