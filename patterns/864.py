# QID: 864
# 
# Generate a solid rectangle using stars. 
# 
# Given an integer R indicates no of rows and an integer C indicates no of columns.Where 1<=R<=100 and Where 1<=C<=100.
# 
# Print the rectangle using stars with R rows and C columns.
# 
# Sample Input : 
# 3 5
# 
# Sample Output : 
# * * * * *
# * * * * *
# * * * * *
# 


# Solution:


def pattern(r, c):
    for i in range(1, r+1):
        l = []
        for j in range(c):
            l.append('*')
        print(*l)

r, c = map(int, input().split())
pattern(r, c)