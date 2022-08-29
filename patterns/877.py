# QID: 877
# 
# Generate a hollow inverted half pyramid pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the hollow inverted half pyramid pattern using numbers based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     1
#    1 2
#   1   3
#  1     4
# 1 2 3 4 5
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = "")
        if i == 1:
            print(1)
        elif i == n:
            l = []
            for j in range(1, n+1):
                l.append(j)
            print(*l)
        else:
            l = ['1']
            for j in range(1, i-1):
                l.append(' ')
            l.append(str(i))
            print(*l)
n = int(input())
pattern(n)