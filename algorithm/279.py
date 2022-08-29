# QID: 279
# 
# Given a number N followed by an array of N integers, every element appears twice except for one. Find that single one and print it. 
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 30 5 5 30 -45
# OUTPUT
# -45
# 
# 
# 
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
for x in a:
  if a.count(x) == 1:
    print(x)
  else:
    pass