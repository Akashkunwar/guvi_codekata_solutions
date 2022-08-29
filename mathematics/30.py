# QID: 30
# 
# Given a number N, find the nearest greater multiple of 10.
# Input Size : N <= 10000
# 
# 
# Sample Testcase :
# INPUT
# 3
# OUTPUT
# 10
# 
# 
# 
# 


# Solution:


a = int(input())
for x in range(a,a+10):
  if x%10==0:
    print(x)