# QID: 34
# 
# Given 2 numbers N and K followed by N elements, find the Kth smallest element.If the element cannot be found then print -1 
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5 2
# 1 1 2 4 5
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = int(a)
b = int(b)
c = [int(i) for i in input().split(' ')]
try:
  print(list(set(c))[b-1])
except:
  print(-1)