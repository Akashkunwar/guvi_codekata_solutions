# QID: 866
# 
# Write a code to generate a pyramid pattern using stars from the given input size N.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the star pyramid with the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# *
# * *
# * * *
# * * * *
# * * * * *
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        l = []
        for j in range(i):
            l.append('*')
        print(*l)
        
n = int(input())
pattern(n)