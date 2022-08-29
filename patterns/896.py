# QID: 896
# 
# Write a code to generate a half pyramid pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the number half pyramid pattern with the size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 1
# 24
# 135
# 2468
# 13579
# 


# Solution:


def pattern(n):
    o = ['1']
    e = ['2']
    for i in range(1, n+1):
        if i % 2 == 1:
            print(''.join(o))
        else:
            print(''.join(e))
        o.append(str(int(o[-1]) + 2))
        e.append(str(int(e[-1]) + 2))
            
n = int(input())
pattern(n)