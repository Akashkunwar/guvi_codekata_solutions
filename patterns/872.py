# QID: 872
# 
# Generate a half diamond pattern using stars and numbers in a palindromic pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the half diamond pattern using stars and numbers in a palindromic pattern based on the given integer R.
# 
# Sample Input : 
# 3
# 
# Sample Output : 
# *
# *1*
# *121*
# *12321*
# *121*
# *1*
# *
# 


# Solution:


def pattern(n):
    print('*')
    for i in range(1, n+1):
        l = []
        l.append('*')
        for j in range(1, i+1):
            l.append(str(j))
        for j in range(i-1, 0, -1):
            l.append(str(j))
        l.append('*')
        print(''.join(l))
    for i in range(n-1, 0, -1):
        l = []
        l.append('*')
        for j in range(1, i+1):
            l.append(str(j))
        for j in range(i-1, 0, -1):
            l.append(str(j))
        l.append('*')
        print(''.join(l))
    print('*')
    
n = int(input())
pattern(n)