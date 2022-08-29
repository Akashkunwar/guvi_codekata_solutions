# QID: 888
# 
# Generate a number pyramid pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100
# 
# Print the number half pyramid pattern with the size R.
# 
# 
# Sample Input : 
# 4
# 
# Sample Output : 
# 1234567
# 12345
# 123
# 1
# 


# Solution:


def pattern(n):
    for i in range(n, 0, -1):
        l = []
        for j in range(1, (2*i)):
            l.append(str(j))
        print(''.join(l))
        
n = int(input())
pattern(n)