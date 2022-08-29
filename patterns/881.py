# QID: 881
# 
# Generate the following pattern.
# 
# *****
# 
# b****
# 
# bb***
# 
# bbb**
# 
# bbbb*
# 
# Input consists of a single integer that corresponds to n, the number of rows.where 1<=n<=100.
# 
# Print the character pattern from the given input n.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# *****
# b****
# bb***
# bbb**
# bbbb*
# 


# Solution:


def pattern(n):
    for i in range(n):
        for j in range(i):
            print('b', end = "")
        for j in range(n-i):
            print('*', end = "")
        print()
        
n = int(input())
pattern(n)