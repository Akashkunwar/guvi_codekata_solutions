# QID: 145
# 
# Given a input string S, reverse the given string by appending each character of the string with '-'.
# Input Size : |S| <= 100000
# 
# 
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# a-t-a-k-e-d-o-c
# 
# 
# 
# 


# Solution:


a = list(input())
a = a[::-1]
b = []
for x in a:
  b.append(x)
  b.append("-")
print(*b[:-1],sep="")