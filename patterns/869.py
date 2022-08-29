# QID: 869
# 
# Write a code to generate an inverted full pyramid pattern using stars.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the star inverted full pyramid with the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# 


# Solution:


def pattern(n):
    for i in range(n):
        for j in range(i):
            print(' ', end = "")
        l = []
        for j in range(n-i):
            l.append('*')
        print(' '.join(l))
        
n = int(input())
pattern(n)