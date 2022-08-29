# QID: 913
# 
# Write a code to generate a aplhabet half pyramid pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=26.
# 
# Print the alphabet half pyramid pattern according to the given integer R.
# 
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# ABCDE
#  ABCD
#   ABC
#    AB
#     A
# 


# Solution:


def pattern(n):
    for i in range(n):
        for j in range(i):
            print(' ', end = "")
        for j in range(n-i):
            print(chr(65+j), end = "")
        print()
n = int(input())
pattern(n)