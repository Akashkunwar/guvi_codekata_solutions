# QID: 98
# 
# Given a number N, print the even factors of N.If the even factor does not exists for N print '-1'.
# Input Size : 1 <= N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 8
# OUTPUT
# 2 4 8
# 
# 
# 
# 


# Solution:


a = int(input())
b = []
for x in range(2,a+1,2):
  if a%x==0:
    b.append(x)
  else:
    pass
if len(b)>0:
  print(*b)
else:
  print(-1)