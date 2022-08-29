# QID: 267
# 
# Given a number N and an array of N elements, print the number of lucky numbers in the array.
# Lucky number: N*I is also present in the array then the number is lucky where N is the number of elements in the array and I is the position of the element.(1 based indexing)
# Input Size : 1 <= N, I <= 100000
# Sample Testcases :
# INPUT
# 5
# 1 2 3 4 5
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


bb = int(input())
a = [int(i) for i in input().split()]
c = []
for x in range(1,bb+1):
  if bb*x in a:
    c.append(x)
  else:
    pass
print(len(c))