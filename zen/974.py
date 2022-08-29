# QID: 974
# 
# Given a number m and k separated by a space print the numbers between m and k
# 
# number m and n separated by a space
# 0<m<1000
# 0<n<1000
# m<n
# 
# 
# print the numbers between this two numbers
# 
# Sample Input : 
# 5 8
# 
# Sample Output : 
# 6 7
# 


# Solution:


a = [int(i) for i in input().split()]
b = []
for x in range(a[0]+1,a[1]):
    b.append(x)
print(*b)