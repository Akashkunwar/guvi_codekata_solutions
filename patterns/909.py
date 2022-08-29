# QID: 909
# 
# Write a code to generate a pyramid pattern on numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the pyramid number pattern based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     0
#    101
#   21012
#  3210123
# 432101234
# 


# Solution:


def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end = "")
            
        for j in range(i, -1, -1):
            print(j, end = "")
        for j in range(1, i+1):
            print(j, end = "")
        print()
n = int(input())
pattern(n)