# QID: 105
# 
# Given a string S and an integer K, print the string obtained by rotating the orignal string by K positions.
# Input Size : 1 <= N, K <= 100000
# 
# 
# Sample Testcase :
# INPUT
# katacode 4
# OUTPUT
# codekata
# 
# 
# 
# 


# Solution:


a,b = input().split()
b = int(b)
c = a[:b]
d = a[b:]
print(d+c)