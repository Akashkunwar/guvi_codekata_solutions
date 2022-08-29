# QID: 202
# 
# Given the values of a,b and x in the equation ax + b = y. Find the value of y.
# 
# 
# Sample Testcase :
# INPUT
# 3 5 2
# OUTPUT
# 11
# 
# 
# 
# 


# Solution:


a,b,x = map(int,input().split(" "))
y = (a*x) + b
print(y)