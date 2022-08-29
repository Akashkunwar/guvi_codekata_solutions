# QID: 889
# 
# Write a code to generate a inverted half pyramid pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100
# 
# Print the number half pyramid pattern with the size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 12345
# 1234
# 123
# 12
# 1
# 


# Solution:


def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end = "")
        print()
n = int(input())
pattern(n)