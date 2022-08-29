# QID: 890
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
# 12345
# 2345
# 345
# 45
# 5
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        for j in range(i, n+1):
            print(j, end = "")
        print()
        
n = int(input())
pattern(n)