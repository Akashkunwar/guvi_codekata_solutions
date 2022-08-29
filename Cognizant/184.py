# QID: 184
# 
# Given 2 numbers N,K and an array of N integers, find if the element K exists in the array.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5 2
# 1 2 3 4 5
# OUTPUT
# yes
# HINT: Read about Binary Search
# 
# 
# 
# 


# Solution:


a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]
if a[1] in b:
    print("yes")
else:
    print("no")