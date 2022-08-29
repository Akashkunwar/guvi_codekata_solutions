# QID: 66
# 
# Given 2 strings,check whether it is isomorphic.If it is not isomorphic print '-1'.
# Input Size : |s| <= 100000(complexity O(nlogn))
# 
# 
# Sample Testcase :
# INPUT
# aab xxy
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b = input().split()

a = list(a)
b = list(b)

c = []
d = []

for x in a:
  c.append(a.count(x))
for x in b:
  d.append(b.count(x))

if c==d:
  print('yes')
else:
  print('no')