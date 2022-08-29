# QID: 212
# 
# Given a number N and an array of N integers, find the sum of all the negative numbers in the array.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 2
# 3 0
# OUTPUT
# 0
# 
# 
# 
# 


# Solution:


a = int(input())
a1 = [int(i) for i in input().split(" ")]
b = []
for x in a1:
  if x<0:
    b.append(x)
print(sum(b))