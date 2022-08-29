# QID: 111
# 
# Given a number N and an array of N elements ,find the Bitwise AND of the array elements.
# Input Size N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 4
# 4 3 2 1
# OUTPUT
# 0
# 
# 
# 
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
b = a[0]
for x in a:
  b &= x
print(b)