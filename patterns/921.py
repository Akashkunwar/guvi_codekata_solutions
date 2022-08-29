# QID: 921
# 
# Write a code to generate a pyramid of numbers and aplhabets.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100
# 
# Print the number half pyramid pattern of multiples based on the given integer R.
# 
# Sample Input : 
# 8
# 
# Sample Output : 
#        A1
#       AB12
#      ABC123
#     ABCD1234
#    ABCDE12345
#   ABCDEF123456
#  ABCDEFG1234567
# ABCDEFGH12345678
# 


# Solution:


def pattern(n):
    c = 64
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = "")
        for j in range(1, i+1):
            print(chr(c+j), end = "")
        for j in range(1, i+1):
            print(j, end = "")
        print()
n = int(input())
pattern(n)