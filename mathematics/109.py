# QID: 109
# 
# Given a number N, print 'INT' if it is integer range or print 'LONG' if it is greater.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 999
# OUTPUT
# INT
# 
# 
# 
# 


# Solution:


a = int(input())
if a>=1 and a<=100000:
  print('INT')
else:
  print('LONG')