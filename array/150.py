# QID: 150
# 
# Given a number N, print all the prime factors once in ascending order.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 100
# OUTPUT
# 2 5
# 
# 
# 
# 


# Solution:


a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
b = int(input())
c= []
for x in a:
  if b%x==0:
    c.append(x)
  else:
    pass
print(*c)