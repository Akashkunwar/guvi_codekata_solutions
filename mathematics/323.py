# QID: 323
# 
# Given a number N print the right-angled triangle with the top level having N 1's followed by each level with is one 1 lesser.
# Input Size : N <= 1000
# 
# 
# Sample Testcase :
# INPUT
# 3
# OUTPUT
# 1 1 1
# 1 1
# 1
# 
# 
# 
# 


# Solution:


n = int(input())
for i in range(n,0,-1) :
    L = [1]*i
    print(*L)