# QID: 244
# 
# Given a number N followed by N numbers. Out of these N numbers some of them are repeated. Write a program to find the first number which is repeated. If no numbers are repeated print 'unique'.
# Input Size : 1 <= N <= 100000
# Sample Testcases :
# INPUT
# 7
# 1 2 3 2 3 4 3
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


aa = input()
b = 'unique'
a = [int(i) for i in input().split()]
for x in a:
  if a.count(x)>1:
    b = x
    break
  else:
    pass
print(b)