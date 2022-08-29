# QID: 49
# 
# Given a number N and an array of N elements, find the length of the longest repeating sequence of the elements.If no such sequence is found print -1
# Input Size : N <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# 8
# 1 2 2 2 3 4 5 6
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
b = 1
c = 0
for x in range(0,len(a)):
  try:
    if a[x]==a[x+1]:
      c = c+1
    else:
      b = b+c
      c = 0
  except:
    pass
if b==1:
    print(-1)
else:
    print(b)