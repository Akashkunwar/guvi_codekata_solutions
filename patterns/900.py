# QID: 900
# 
# Write a code to generate the hollow diamond inscribed in a rectangle using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the hollow diamond in a rectangle using stars with the size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# 


# Solution:


def pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end = "")
        for j in range(2*(n-i)):
            print(' ', end = "")
        for j in range(i):
            print('*', end = "")
            
        print()
    for i in range(1, n+1):
        for j in range(i):
            print('*', end = "")
        for j in range(2*(n-i)):
            print(' ', end = "")
        for j in range(i):
            print('*', end = "")
            
        print()
n = int(input())
pattern(n)