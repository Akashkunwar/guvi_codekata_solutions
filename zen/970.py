# QID: 970
# 
#  Given a two number n and m find the Quotient and remainder
# 
# 0<n<10000
# 0<m<10000
# Given two number separated by a space
# 
# 
# Need to print Quotient and remainder separated by a space
# 
# 
# Sample Input : 
# 6 3
# 
# Sample Output : 
# 2 0
# 


# Solution:


a,b = input().split()
a = int(a)
b = int(b)
print(a//b,a%b)