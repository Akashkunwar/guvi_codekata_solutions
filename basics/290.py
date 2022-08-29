# QID: 290
# 
# Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 2 3 4 5
# OUTPUT
# 1 5
# 
# 
# 
# 


# Solution:


b=input()
a=list(map(int, input().split(" ")))
min=min(a)
max=max(a)
print(a.index(min)+1,a.index(max)+1)