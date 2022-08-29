# QID: 895
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
# 13579
# 3579
# 579
# 79
# 9
# 


# Solution:


def pattern(n):
    for i in range(1, (2*n), 2):
        l = []
        for j in range(i, 2*n, 2):
            l.append(str(j))
        print(''.join(l))
    
n = int(input())
pattern(n)