# QID: 73
# 
# Given a number N, print the sum of the squares of its digits.
# Input Size : 1 <= N <= 1000000000000000000
# 
# 
# Sample Testcase :
# INPUT
# 19
# OUTPUT
# 82
# 
# 
# 
# 


# Solution:


num = int(input())
sum = 0
while num!=0:
    rem = num%10
    sqr = rem*rem
    sum = sum+sqr
    num = int(num/10)
print(sum)