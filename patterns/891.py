# QID: 891
# 
# Write a code to generate a half pyramid pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100
# 
# Print the number half pyramid pattern with the size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 54321
# 4321
# 321
# 21
# 1
# 


# Solution:


def pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end = "")
        print()
n = int(input())
pattern(n)