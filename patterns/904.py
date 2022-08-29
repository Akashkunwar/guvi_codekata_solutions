# QID: 904
# 
# Write a code to generate a pyramid using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the pyramid pattern using stars based on the given integer R.
# 
# Sample Input : 
# 6
# 
# Sample Output : 
#      *
#     **
#    ***
#   ****
#  *****
# ******
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        for j in range(n - i):
            print(" ", end = "")
        for j in range(i):
            print("*", end = "")
        print()

n = int(input())
pattern(n)