# QID: 180
# 
# Given an array N, sort it in ascending order till it reaches kth elements and after that sort it in descending order.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 5 2
# 4 3 1 2 4
# OUTPUT
# 3 4 4 2 1
# 
# 
# 
# 


# Solution:


a,b = input().split()
b = int(b)
c = [int(i) for i in input().split(' ')]
d = c[:b]
d = sorted(d)
e = c[b:]
e = sorted(e)[::-1]
f = d+e
print(*f)