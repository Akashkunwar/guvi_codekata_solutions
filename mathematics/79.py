# QID: 79
# 
# Given a number N, print their prime factors in sorted order.
# Input Size : 2 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 18
# OUTPUT
# 2 3
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
print(*ans)