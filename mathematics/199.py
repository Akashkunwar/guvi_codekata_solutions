# QID: 199
# 
# Given 3 numbers A,B,C print 'yes' if they can form the sides of a right angled triangle,otherwise 'no'.
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


a,b,c = map(int, input().split())
if (a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2):
  print("yes")
else:
  print("no")