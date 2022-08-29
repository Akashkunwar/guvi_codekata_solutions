# QID: 19
# 
# Write a program to calculate the total surface area and volume of cuboid. Input contains three space separated positive integers L, B, H denoting the length, width and height of cuboid respectively.
# 
# 
# Sample Testcase :
# INPUT
# 1 2 3
# OUTPUT
# 22 6
# 
# 
# 
# 


# Solution:


a,b,c = map(int,input().split())
ts = (a*b)+(b*c)+(a*c)
tsa = 2*ts
volume = a*b*c
print(*[tsa,volume])