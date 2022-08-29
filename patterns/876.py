# QID: 876
# 
# Generate a hollow inverted half pyramid pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the hollow Inverted half pyramid pattern using numbers based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 12345
# 1  4
# 1 3
# 12
# 1
# 


# Solution:


def pattern(n):
    for i in range(n, 0, -1):
        a = ''
        if i == 1:
            a += str(i)
        elif i == n:
            for i in range(1, n+1):
                a += str(i)
        else:
            a += '1'
            a += ' '*(i-2)
            a += str(i)
        print(a)

n = int(input())
pattern(n)