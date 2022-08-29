# QID: 148
# 
# Given a number N and an array of N strings, find the lexicographically smallest string.
# Input Size : N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 3
# code
# learn
# practice
# OUTPUT
# code
# 
# 
# 
# 


# Solution:


a = int(input())
b=[]

for x in range(0,a):
  b.append(input())
b = sorted(b)
print(b[0])