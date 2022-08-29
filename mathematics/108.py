# QID: 108
# 
# Given a number N, print the odd factors for the N.
# Input Size : 1 <= N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 9
# OUTPUT
# 1 3 9
# 
# 
# 
# 


# Solution:


a = []
def print_factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            a.append(i)

num = int(input())

print_factors(num)
b = []
for x in a:
  if x%2!=0:
    b.append(x)
print(*b)