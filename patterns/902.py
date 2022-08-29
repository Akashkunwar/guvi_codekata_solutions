# QID: 902
# 
# Write a code to generate a left arrow pattern using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# 
# Print the left arrow pattern based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# *
#  *
#   *
#    *
# *****
#    *
#   *
#  *
# *
# 


# Solution:


def pattern(n):
    for i in range(n-1):
        for j in range(i):
            print(' ', end = "")
        print('*')
    print('*' * n)
    for i in range(n-2, -1, -1):
        for j in range(i):
            print(' ', end = "")
        print('*')
n = int(input())
pattern(n)