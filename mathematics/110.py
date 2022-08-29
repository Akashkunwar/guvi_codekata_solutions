# QID: 110
# 
# Given a number N, check if N is divisible by any number less than N (ie.,it leaves no remainder)except 1.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 10
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = int(input())
b = []
for x in range(2,a):
  if a%x==0:
    b.append('x')
  else:
    pass
if len(b)>0:
  print('yes')
else:
  print('no')