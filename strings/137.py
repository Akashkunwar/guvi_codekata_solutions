# QID: 137
# 
# Given a number N and an array of N elements, print the prefix sum array.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 4
# 2 4 4 2
# OUTPUT
# 2 6 10 12
# 
# 
# 
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
c = []
def add(mylist):
  b = 0
  for x in a:
    b = b + x
    c.append(b)
  return c
print(*add(c))