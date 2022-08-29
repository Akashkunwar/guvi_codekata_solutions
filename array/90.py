# QID: 90
# 
# Given 2 strings and a number K, check whether they differ exactly by K characters.
# Input Size : |s| <= 100000(complexity O(nlogn) or O(n))
# 
# 
# Sample Testcase :
# INPUT
# codekata codeguvi 4
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b,z = input().split()
a = list(a)
b = list(b)
z = int(z)
c = []
for x,y in zip(a,b):
  if x==y:
    c.append(0)
  else:
    c.append(1)

d = sum(c)
if z==d:
  print('yes')
else:
  print('no')