# QID: 104
# 
# Given 2 numbers P and A which are the perimeter and area of a rectangle respectively, find if there can actually be a rectangle with this perimeter and area having integer sides.If there exists such rectangle print 'yes' otherwise print 'no'.
# Input Size : 1 <= P,A <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 20 25
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


p,a = input().split()
p = int(p)
a = int(a)
c = []
for x in range(2,a):
  if a%x==0:
    c.append(x)
  else:
    pass
d = []
for x in c:
  for y in c:
    if 2*(x+y)==p and x*y==a:
      d.append(1)
    else:
      d.append(0)
if 1 in d:
  print('yes')
else:
  print('no')