# QID: 50
# 
#  Given 2 numbers N,K print the array after deleting the last K elements.
# Input Size : N,K <= 100000 
# 
# 
# Sample Testcase :
# INPUT
# 5 4
# 1 2 3 4 5
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


a,b = input().split()
c = [int(i) for i in input().split()]
b = int(b)
c = c[::-1]
d = c[b:]
d = d[::-1]
print(*d)