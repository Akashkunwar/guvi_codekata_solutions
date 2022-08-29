# QID: 905
# 
# Write a code to generate a pyramid using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the pyramid pattern using stars based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# *****
#  ****
#   ***
#    **
#     *
# 


# Solution:


def pattern(n):
    for i in range(n):
        l = []
        for j in range(i):
            l.append(' ')
        for j in range(n-i):
            l.append('*')
        print(''.join(l))
        
n = int(input())
pattern(n)