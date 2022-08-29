# QID: 887
# 
# Write a code to generate a half pyramid number pattern.
# 
# Given an even integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the number half pyramid pattern with the size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 12345
# 4321
# 123
# 21
# 1
# 


# Solution:


def pattern(n):
    for i in range(n):
        if i % 2 == 0:
            for j in range(n-i):
                print(j+1, end = "")
        else:
            for j in range(n-i, 0, -1):
                print(j, end = "")
        print()
n = int(input())
pattern(n)