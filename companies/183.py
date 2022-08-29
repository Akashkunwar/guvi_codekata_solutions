# QID: 183
# 
# Given a number N and an array of N strings,Print yes, if all strings have atleast one vowel in them otherwise print no.
# Input Size : N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 5
# code
# overload
# vishal
# sundar
# anish
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


a = int(input())
b = []
for x in range(0,a):
  b.append(input())
c = []
for x in b:
  if ("a" or "e" or "i" or "o" or "u") in list(x.lower()):
    c.append(1)
  else:
    c.append(0)
if 0 in c:
  print("no")
else:
  print("yes")