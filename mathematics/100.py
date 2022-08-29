# QID: 100
# 
# Given a number N, check if it is a power of 2.Print 'yes' if it is a power of 2 otherwise print 'no'.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 64
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


import math
a = math.sqrt(int(input()))
if a.is_integer() == True:
  print('yes')
else:
  print('no')