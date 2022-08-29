# QID: 65
# 
# Given a roman numeral N, convert it into integer.Take L=50, C=100.If it is not a valid roman numeral print '-1'
# Input Size : N <= 100
# 
# 
# Sample Testcase :
# INPUT
# VI
# OUTPUT
# 6
# INPUT
# Y
# OUTPUT
# -1
# 
# 
# 
# 


# Solution:


I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
a = input()
a = list(a)
b = []
for x in a:
  if x=='I':
    b.append(1)
  elif x=='V':
    b.append(5)
  elif x=='X':
    b.append(10)
  elif x=='L':
    b.append(50)
  elif x=='C':
    b.append(100)
  elif x=='D':
    b.append(500)
  elif x=='M':
    b.append(1000)
z = sum(b)
if z==0:
  print(-1)
else:
  print(z)