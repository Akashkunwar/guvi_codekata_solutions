# QID: 32
# 
# Write a program to print the sum of the first K natural numbers.
# Input Size : n <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 3
# OUTPUT
# 6
# 
# 
# 
# 


# Solution:


a = []
b=int(input())
for x in range(b+1):
  a.append(x)
print(sum(a))