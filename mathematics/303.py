# QID: 303
# 
# Given a number N, print the sum of squares of all its digits.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# 12
# OUTPUT
# 5
# 
# 
# 
# 


# Solution:


a = [str(d) for d in str(input())]
b = list(map(int, a))
def square(list):
    return [i ** 2 for i in list]
print(sum(square(b)))