# QID: 897
# 
# Write a code to generate a square pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# 
# Print the number pattern separated with space with the size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 5 5 5 5 5
# 4 5 5 5 5
# 3 4 5 5 5
# 2 3 4 5 5
# 1 2 3 4 5
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        l = []
        for j in range(n-i+1, n+1):
            l.append(j)
        for j in range(n-i):
            l.append(n)
        print(*l)
        
n = int(input())
pattern(n)