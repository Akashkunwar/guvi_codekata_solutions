# QID: 976
# 
# Given a number m and k separated by a space print n numbers which multiple of m
# 
# number m and k separated by a space
# 0<n<1000
# 0<m<1000
# 
# print n numbers which multiple of m
# 
# Sample Input : 
# 5 4
# 
# Sample Output : 
# 4 8 12 16 20
# 


# Solution:


a = [int(i) for i in input().split()]
b = []
for x in range(1,a[0]+1):
  b.append(a[1]*x)
print(*b)