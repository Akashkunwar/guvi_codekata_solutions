# QID: 1
# 
# Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
# 
# 
# Sample Testcase :
# INPUT
# 9 2
# OUTPUT
# odd
# 
# 
# 
# 


# Solution:


a,b = map(int, input().split(" "))
c = a+b
if c%2==0:
    print("even")
else:
    print("odd")