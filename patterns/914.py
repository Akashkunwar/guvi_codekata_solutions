# QID: 914
# 
# Write a code to generate a aplhabet half pyramid pattern.
# 
# Given an integer R indicates number of rows.Where 1<=R<=26.
# 
# Print the alphabet half pyramid pattern according to the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# EEEEE
#  DDDD
#   CCC
#    BB
#     A
# 


# Solution:


def pattern(n):
    for i in range(n):
        for j in range(i):
            print(' ', end = "")
        print(chr(65+n-i-1) * (n-i))
        
n = int(input())
pattern(n)