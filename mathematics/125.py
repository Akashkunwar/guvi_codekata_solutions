# QID: 125
# 
# Given a number N, print the sum of its first and last digit.
# Input Size : |N| <= 10000
# 
# 
# Sample Testcase :
# INPUT
# 51233
# OUTPUT
# 8
# 
# 
# 
# 


# Solution:


a = input()
b=list(a)
print(int(b[0])+int(b[-1]))