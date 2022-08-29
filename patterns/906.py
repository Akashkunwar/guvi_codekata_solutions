# QID: 906
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
# 999999999
#  7777777
#   55555
#    333
#     1
# 


# Solution:


def pattern(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(' ', end = "")
        for j in range((2*i)-1):
            print((2*i)-1, end = "")
        print()
        
n = int(input())
pattern(n)