# QID: 922
# 
# Write a code to generate a square pattern using the number &#39;1&#39;.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the square pattern with the number '1' in R*R form based on the given integer R.
# 
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 11111
# 11111
# 11111
# 11111
# 11111
# 


# Solution:


def pattern(n):
    for i in range(n):
        print('1'*n)

n = int(input())
pattern(n)