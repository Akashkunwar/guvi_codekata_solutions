# QID: 99
# 
# Given a number N, print the distinct pairs formed by multiplying two prime numbers (i.e)prime x prime should yield the N.Also print the numbers in descending order.If no such pairs can be formed print '-1'.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 65
# OUTPUT
# 13 5
# 
# 
# 
# 


# Solution:


num=int(input())
factors=[]
for i in range(1,num+1):
    if num%i==0:
       factors.append(i)
pr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
ans = []
for x in factors:
  if x in pr:
    ans.append(x)
  else:
    pass
ans = ans[::-1]
if len(ans)>1:
  print(*ans)
else:
  print(-1)