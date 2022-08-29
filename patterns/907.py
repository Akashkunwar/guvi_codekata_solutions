# QID: 907
# 
# Write a code to generate a aplhabet pyramid pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=26.
# 
# Print the alphabet pyramid pattern according to the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
#     A
#    ABA
#   ABCAB
#  ABCDABC
# ABCDEABCD
# 


# Solution:


def pattern(n):
    c = 65
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = "")
        for j in range(i):
            print(chr(c+j), end = "")
        for j in range(i-1):
            print(chr(c+j), end = "")
        print()
n = int(input())
pattern(n)