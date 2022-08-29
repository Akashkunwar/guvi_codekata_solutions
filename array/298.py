# QID: 298
# 
# Given a number N, print all prime numbers less than N(in ascending order).
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 10
# OUTPUT
# 2 3 5 7
# 
# 
# 
# 


# Solution:


a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
b = int(input())
a.append(b)
a = sorted(a)
c = a.index(b)
d = a[:c]
print(*d)