# QID: 871
# 
# Write a code to generate a solid half diamond pattern using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the solid half diamond pattern based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        l = []
        for j in range(i):
            l.append('*')
        print(''.join(l))
    for i in range(1, n):
        l = []
        for j in range(n-i):
            l.append('*')
        print(''.join(l))
        
n = int(input())
pattern(n)