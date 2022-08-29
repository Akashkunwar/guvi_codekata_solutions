# QID: 11
# 
# Given a number N, print its factors.
# Input Size : n<=1000 
# 
# 
# Sample Testcase :
# INPUT
# 6
# OUTPUT
# 1 2 3 6
# 
# 
# 
# 


# Solution:


num=int(input())
factors=[]
for i in range(1,num+1):
    if num%i==0:
       factors.append(i)

print (*factors)