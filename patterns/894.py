# QID: 894
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
# 55555
# 4444
# 333
# 22
# 1
# 


# Solution:


def pattern(n):
    for i in range(n, 0, -1):
        l = []
        for j in range(i):
            l.append(str(i))
        print(''.join(l))

n = int(input())
pattern(n)