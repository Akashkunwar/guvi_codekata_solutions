# QID: 242
# 
# Given a number N followed by N numbers. All the numbers in the given input appear twice except for one number(ie one number appears only once in the given input). Find the number which appears only once.
# Input Size : 1 <= N <= 100000
# Sample Testcases :
# INPUT
# 5
# 1 2 1 3 2
# OUTPUT
# 3 
# 
# 
# 
# 


# Solution:


bb = int(input())
a = [int(i) for i in input().split()]
for x in a:
  if a.count(x)==1:
    print(x)
    break
  else:
    pass