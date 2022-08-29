# QID: 1016
# 
# Given a numbers n followed by n*n numbers in matrix format print the sum of the numbers in the row
# 
# You will given a number n followed by n*m numbers in matrix format .
# 
# print the sum of the numbers in the row
# 
# Sample Input : 
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 
# Sample Output : 
# 6 15 24
# 


# Solution:


a,b = input().split()
a = int(a)
b = int(b)
c = []
for x in range(0,a):
  c.append([int(i) for i in input().split()])
d = []
for x in c:
  d.append(sum(x))
print(*d)