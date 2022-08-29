# QID: 892
# 
# Write a code to generate a half pyramid pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100
# 
# 
# Print the number half pyramid pattern with the size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 5
# 45
# 345
# 2345
# 12345
# 


# Solution:


def pattern(n):
    for i in range(n, 0, -1):
        l = []
        for j in range(i, n+1):
            l.append(str(j))
        print(''.join(l))
        
n = int(input())
pattern(n)