# QID: 899
# 
# Write a code to generate an hollow rhombus Pattern using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the solid rhombus using stars with the size R.
# 
# Sample Input : 
# 4
# 
# Sample Output : 
#    ****
#   *  *
#  *  *
# ****
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = "")
        if i == 1 or i == n: print('*' * n)
        else:
            s = '*'
            s += ' ' * (n-2)
            s += '*'
            print(s)
n = int(input())
pattern(n)