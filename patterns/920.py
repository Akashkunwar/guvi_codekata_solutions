# QID: 920
# 
# Write a code to generate a half pyramid pattern of mulitples of the given number.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the number half pyramid pattern of multiples based on the given integer R.
# 
# Sample Input : 
# 10
# 
# Sample Output : 
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64
# 9 18 27 36 45 54 63 72 81
# 10 20 30 40 50 60 70 80 90 100
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        l = []
        for j in range(1, i+1):
            l.append(i*j)
        print(*l)
        
n = int(input())
pattern(n)