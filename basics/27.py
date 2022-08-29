# QID: 27
# 
# Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
# 
# 
# Sample Testcase :
# INPUT
# 6 2
# 1 2 3 5 7 8
# OUTPUT
# 0
# 
# 
# 
# 


# Solution:


a,b = map(int,input().split(" "))
n = [int(i) for i in input().split(" ")]
m = n.count(b)
if b in n:
  print(m-1)
else:
  print(-1)