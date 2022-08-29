# QID: 14
# 
# Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.
# Input Size : N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 2143
# OUTPUT
# 1 3
# 
# 
# 
# 


# Solution:


a = input()
n = int(a)
arr = []
for i in a:
    if int(i) % 2 == 1:
        arr.append(i)
    n = n // 10 
if len(arr) >= 1:
    print(*arr)
else:
    print(-1)