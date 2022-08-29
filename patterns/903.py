# QID: 903
# 
# Write a code to generate a right arrow using patterns.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the right arrow pattern using stars based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     *
#    *
#   *
#  *
# *****
#  *
#   *
#    *
#     *
# 


# Solution:


def pattern(n):
    for i in range(n-1):
        for j in range(n-i-1):
            print(' ', end = "")
        print('*')
    print('*' * n)
    for i in range(n-2, -1, -1):
        for j in range(n-i-1):
            print(' ', end = "")
        print('*')
n = int(input())
pattern(n)