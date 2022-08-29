# QID: 20
# 
# Given a number N, print its reverse.
# Input Size : n <= 1000 
# 
# 
# Sample Testcase :
# INPUT
# 10
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


a = int(input())
b = list(str(a))[::-1]
c = [int(i) for i in b]
if c[0]==0:
  d=c[1:]
else:
  d=c
print(*d, sep = "")