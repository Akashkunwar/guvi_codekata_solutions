# QID: 883
# 
# Wrrite a code to generate the following pattern.
# 
# bbbb*bbbb
# 
# bbb***bbb
# 
# bb*****bb
# 
# b*******b
# 
# *********
# 
# b*******b
# 
# bb*****bb
# 
# bbb***bbb
# 
# bbbb*bbbb
# 
# Given an odd integer R indicates number of rows.R is always an odd number.where 1<=R<=100.
# 
# Print the character pattern based on the given input R.
# 
# Sample Input : 
# 9
# 
# Sample Output : 
# bbbb*bbbb
# bbb***bbb
# bb*****bb
# b*******b
# *********
# b*******b
# bb*****bb
# bbb***bbb
# bbbb*bbbb
# 


# Solution:


def pattern(n):
    for i in range(1, n):
        l = []
        for j in range(n-i):
            l.append('b')
        for j in range(2*(i-1)+1):
            l.append('*')
        for j in range(n-i):
            l.append('b')
        print(''.join(l))
    for i in range(n):
        l = []
        for j in range(i):
            l.append('b')
        for j in range(2*(n-i)-1):
            l.append('*')        
        for j in range(i):
            l.append('b')
        print(''.join(l))
        
n = int(input())
pattern((n+1)//2)