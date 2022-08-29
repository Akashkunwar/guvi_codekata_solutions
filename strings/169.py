# QID: 169
# 
# Given 2 numbers N,K and an array of N strings, find if any K consecutive strings are same.
# Input Size : K <= N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 5 3
# code
# overload
# vishal
# vishal
# vishal
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
  c.append(input())
  
d = []
for x in c:
  d.append(c.count(x))

for x in d:
  if x==b:
    z = 1
  else:
    z = 0

if z==1:
  print("yes")
else:
  print("no")