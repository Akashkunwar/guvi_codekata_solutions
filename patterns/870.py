# QID: 870
# 
# Write a code to generate a hollow full pyramid pattern using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the star hollow full pyramid with the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     *
#    * *
#   *   *
#  *     *
# * * * * *
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = "")
        l = []
        if i == 1:
            l.append('*')
        elif i == n:
            for j in range(n):
                l.append('*')
        else:
            l.append('*')
            for j in range(i-2):
                l.append(' ')
            l.append('*')
        print(*l)
        
n = int(input())
pattern(n)