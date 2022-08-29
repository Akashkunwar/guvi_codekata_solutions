# QID: 999
# 
# Given a numbers n followed by x and y array of n number. Add the common number in the array x and y and print the numbers. If there is no such number print -1. A number is said to be a common number if x[i] == y[i].
# 
# 0<n<100
# Given a number n 
# Followed by x number in next line
# Followed by y number in next line
# 
# Print added common numbers if their is no number print -1
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 1 2 3 5 1 1
# 
# Sample Output : 
# -1
# 


# Solution:


aa = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = []
for x in range(0,aa):
  if a[x]==b[x]:
    c.append(a[x])
if len(c)==0:
  print(-1)
else:
  d = sum(c)*2
  print(d)