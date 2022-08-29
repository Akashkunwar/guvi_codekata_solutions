# QID: 222
# 
# Given 3 numbers A,B,C find (A^B)%C.
# Input Size : A,B,C <= 1000000000
# 
# 
# Sample Testcase :
# INPUT
# 3 4 1000000007
# OUTPUT
# 81
# 
# 
# 
# 


# Solution:


a,b,c = map(int, input().split(" "))
d = a**b
e = d%c
print(e)