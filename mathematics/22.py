# QID: 22
# 
# Given 3 numbers a,b,c print a*b mod c.
# 
# 
# Sample Testcase :
# INPUT
# 5 3 2
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


a,b,c = map(int,input().split(" "))
d = a*b
e = d%c
print(e)