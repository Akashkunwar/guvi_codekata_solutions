# QID: 168
# 
# Given a number N and an array of N strings, find if two consecutive words are same.
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
# no
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
  c.append(b.count(x))

if 2 in c:
  print("yes")
else:
  print("no")