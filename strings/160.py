# QID: 160
# 
#  Given 2 numbers n and m, n pairs of numbers a and b are given. In each pair 'a' means a person can start moving from point 'a' in the x axis to point 'b'(he can visit any point in between). Find if he can visit point m.
# 
# 
# Sample Testcase :
# INPUT
# 3 5
# 0 2
# 2 4
# 3 5
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

c = []
for x in range(0,a):
  d,e = input().split()
  c.append(int(d))
  c.append(int(e))

if b in c:
  print("yes")
else:
  print("no")