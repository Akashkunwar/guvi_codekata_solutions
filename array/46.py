# QID: 46
# 
# Given a number N and an array of N elements, print all elements lesser than N in descending order.If no element found print -1
# Input Size : 1 <= N <= 10000
# 
# 
# Sample Testcase :
# INPUT
# 5
# 2 14 15 14 3
# OUTPUT
# 3 2
# 
# 
# 
# 


# Solution:


a = int(input())
aa = [int(i) for i in input().split(" ")]
j2 = [i for i in aa if i < 5]
j2.sort()
if len(j2)==0:
  print(-1)
else:
  print(*j2[::-1],sep=" ")