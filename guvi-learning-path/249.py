# QID: 249
# 
# Given two numbers N,K(N>=K) and an array of N elements, write a program to find the Kth largest element.
# Input Size : 1 <= K <= N <= 100000
# Sample Testcases :
# INPUT
# 6 2
# 1 2 3 4 5 6
# OUTPUT
# 5
# 
# 
# 
# 


# Solution:


a,b = input().split()
b = int(b)
c = [int(i) for i in input().split(' ')]
c = sorted(c)
print(c[-b])