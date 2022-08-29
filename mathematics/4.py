# QID: 4
# 
# Given a number N, find  its next immediate greater power of 2(i.e 2^1, 2^2, 2^3...).
# Input Size : N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 4
# OUTPUT
# 8
# 
# 
# 
# 


# Solution:


import math
a = int(input())
b = int(math.log(a,2))
print(2**(b+1))