# QID: 72
# 
# Given two numbers N,K followed by an array of N elements, print the array after doing right shift K times (in cyclic manner).
# Input Size : 1 <= N, K <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 3 2
# 7 2 3
# OUTPUT
# 2 3 7
# 
# 
# 
# 


# Solution:


b,c = map(int,input().split(" "))
a = [int(i) for i in input().split(" ")]
for x in range(c):
    a = [a[-1]]+a[:-1]
print(*a)