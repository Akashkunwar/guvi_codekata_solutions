# QID: 54
# 
# Given a number N,K followed by array of N elements where the difference between any adjacent elements is 1. Find the position of the given number K.If K not found in the array print -1
# 
# 
# Sample Testcase :
# INPUT
# 5 1
# 3 2 1 2 3
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


a,b = input().split()
c = [int(i) for i in input().split()]
b = int(b)
try:
    print(c.index(b)+1)
except:
    print(-1)