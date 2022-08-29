# QID: 274
# 
# There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Given a number N Count the number of ways, the person can reach the top.
# Input Size : N <= 100
# 
# 
# Sample Testcase :
# INPUT
# 3
# OUTPUT
# 3
# 
# 
# 
# 


# Solution:


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
def countWays(s):
    return fib(s + 1)
s = int(input())
print(countWays(s))