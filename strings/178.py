# QID: 178
# 
#  Given a string and a number K.Print every kth character from the beginning.
# 
# 
# Sample Testcase :
# INPUT
# string 3
# OUTPUT
# r g
# 
# 
# 
# 


# Solution:


a,z = input().split()
z = int(z)
a = list(a)
l = len(a)
b = []
for x in range(z,l+1,z):
  b.append(x)
c = []
for x in b:
  c.append(a[x-1])
print(*c)