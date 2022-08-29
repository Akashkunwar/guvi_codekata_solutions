# QID: 878
# 
# Generate a floyd&#39;s triangle.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print a floyd's triangle based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 


# Solution:


def pattern(n):
    a = 1
    for i in range(1, n+1):
        l = []
        for j in range(i):
            l.append(a)
            a += 1
        print(*l)

n = int(input())
pattern(n)