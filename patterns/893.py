# QID: 893
# 
# Write a code to generate a half pyramid pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the number half pyramid pattern with the size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 1
# 22
# 333
# 4444
# 55555
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        a = str(i)*i
        print(a)
        
n = int(input())
pattern(n)