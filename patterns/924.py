# QID: 924
# 
# Write a code to generate the X form of a number pattern.
# 
# Given an integer N indicates X pattern.Where 1<=N<=100.
# 
# 
# Print the numbers in X form based on the given integer N.Where 1<=N<=100 
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 1       1
#  2     2
#   3   3
#    4 4
#     5
#    4 4
#   3   3
#  2     2
# 1       1
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        for j in range(i-1):
            print(' ', end = "")
        print(i, end = "")
        for j in range(2*(n-i)-1):
            print(' ', end = "")            
        if i != n: print(i)
        else: print()
    for i in range(n-1, 0, -1):
        for j in range(i-1):
            print(' ', end = "")
        print(i, end = "")
        for j in range(2*(n-i)-1):
            print(' ', end = "")            
        if i != n: print(i)
        else: print()
            
n = int(input())
pattern(n)