# QID: 868
# 
# Write a code to generate a full pyramid pattern using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the star pyramid with the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# 


# Solution:


def pattern(n):
    c = 65
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = "")
        l = []
        for j in range(i):
            l.append('*')
        print(*l)
n = int(input())
pattern(n)