# QID: 127
# 
# Given a  number N and a number K, check if it has all digits from 0 to k in it.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 1234034 4
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = list(a)
b = int(b)
a = set(a)
c = []
for x in a:
  c.append(int(x))
c = sorted(c)
d = list(range(0,int(b)+1))
if c==d:
  print('yes')
else:
  print('no')