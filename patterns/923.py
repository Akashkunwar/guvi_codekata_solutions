# QID: 923
# 
# Write a code to generate a half pyramid number pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100
# 
# Print the number half pyramid pattern based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 1
# 2 4
# 1 3 5
# 2 4 6 8
# 1 3 5 7 9
# 


# Solution:


def pattern(n):
    o = ['1']
    e = ['2']
    for i in range(1, n+1):
        if i % 2 == 1:
            print(*o)
        else:
            print(*e)
        o.append(str(int(o[-1]) + 2))
        e.append(str(int(e[-1]) + 2))
            
n = int(input())
pattern(n)