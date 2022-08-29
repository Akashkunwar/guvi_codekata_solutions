# QID: 901
# 
# Write a code to generate a butterfly pattern printing using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# 
# Print the butterfly pattern printing using stars based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end = "")
        for j in range(2*(n-i)):
            print(' ', end = "")
        for j in range(i):
            print('*', end = "")
            
        print()
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end = "")
        for j in range(2*(n-i)):
            print(' ', end = "")
        for j in range(i):
            print('*', end = "")
            
        print()
n = int(input())
pattern(n)