# QID: 239
# 
# Given a number N followed by N numbers. Out of these N numbers some of them are repeated. Write a program to find the number which is repeated and print the repeated numbers in sorted order. If no numbers are repeated print "unique".
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 7
# 1 2 3 2 3 4 3
# OUTPUT
# 2 3
# 
# 
# 
# 


# Solution:


aa = input()
l = [int(i) for i in input().split(" ")]
a = list(set([x for x in l if l.count(x) > 1]))
a = sorted(a)
if len(a)==0:
  print("unique")
else:
  print(*a)