# QID: 916
# 
# Write a code to generate a triangle character pattern.
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
#    A B
#   A B C
#  A B C D
# A B C D E
# 


# Solution:


def pattern(n):
    c = 65
    l = []
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end = "")
        l.append(chr(c + i))
        print(*l)
        
n = int(input())
pattern(n)