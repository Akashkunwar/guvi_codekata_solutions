# QID: 197
# 
# Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.
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
if (a+b>c and b+c>a and c+a>b):
  print("yes")
else:
  print("no")