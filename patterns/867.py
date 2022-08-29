# QID: 867
# 
# Write a code to generate an inverted half pyramid pattern using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the star inverted pyramid with the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
# 


# Solution:


def pattern(n):
    for i in range(n):
        a = []
        for j in range(n-i):
            a.append('*')
        print('  '.join(a))

n = int(input())
pattern(n)