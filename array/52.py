# QID: 52
# 
# Given a number N followed by N elements for every 2 consecutive numbers print the maximum of the 2.
# Input Size : N <= 100000 (ie do it in O(n) time complexity)
# 
# 
# Sample Testcase :
# INPUT
# 5
# 1 1 3 0 5
# OUTPUT
# 1 3 3 5
# 
# 
# 
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
b = []
for x in range(0,len(a)):
  try:
    b.append(max([a[x],a[x+1]]))
  except:
    pass
print(*b)