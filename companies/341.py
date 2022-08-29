# QID: 341
# 
#  Given 2 numbers N and K followed by N numbers such that sum of two pairs in the N numbers results K value, if it exist print 'yes' otherwise 'no'.
# Input Size : N<=100000 
# Example:
# INPUT
# 4 4
# 1 2 2 4
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a,b = input().split()
a = int(a)
b = int(b)
c = [int(i) for i in input().split()]
d = 0
for x in c:
  for y in c:
    if x+y == b:
      d+=1
    else:
      d+=0
if d==0:
  print('no')
else:
  print('yes')