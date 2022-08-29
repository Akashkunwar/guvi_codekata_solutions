# QID: 138
# 
# Given a number N and an array of N elements, print the suffix sum of the array.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 4
# 2 4 4 2
# OUTPUT
# 12 10 6 2
# 
# 
# 
# 


# Solution:


aa = input()
a = [int(i) for i in input().split(" ")]
c = [sum(a)]
def add(mylist):
  b = sum(a)
  for x in a:
    b = b - x
    c.append(b)
  return c
print(*add(c)[:-1])