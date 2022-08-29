# QID: 912
# 
# Write a code to generate a aplhabet pyramid pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=26.
# 
# 
# Print the alphabet pyramid pattern according to the given integer R.
# 
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     A
#    BBB
#   CCCCC
#  DDDDDDD
# EEEEEEEEE
# 


# Solution:


def pattern(n):
    c = 65
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end = "")
        for j in range((2*i)+1):
            print(chr(c+i), end = "")
        print()
n = int(input())
pattern(n)