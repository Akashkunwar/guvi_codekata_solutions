# QID: 898
# 
# Write a code to generate an Rhombus Pattern using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the solid rhombus using stars with the size of rhombus R.
# 
# Sample Input : 
# 4
# 
# Sample Output : 
#    ****
#   ****
#  ****
# ****
# 


# Solution:


def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end = "")
        print('*' * n)
n = int(input())
pattern(n)