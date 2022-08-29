# QID: 884
# 
# write a code to generate the following pattern.
# 
#  
# 
# **********
# 
# ****bb****
# 
# ***bbbb***
# 
# **bbbbbb**
# 
# *bbbbbbbb*
# 
# **bbbbbb**
# 
# ***bbbb***
# 
# ****bb****
# 
# **********
# 
# Given an even integer R indicates number of stars in first and last row.R is always an even number.Where 2<=R<=100.
# 
# Print the pattern based on the given integer R.
# 
# Sample Input : 
# 10
# 
# Sample Output : 
# **********
# ****bb****
# ***bbbb***
# **bbbbbb**
# *bbbbbbbb*
# **bbbbbb**
# ***bbbb***
# ****bb****
# **********
# 


# Solution:


def pattern(n):
    for i in range(n-1):
        l = []
        for j in range(n-i):
            l.append('*')
        for j in range(2*i):
            l.append('b')
        for j in range(n-i):
            l.append('*')
        print(''.join(l))
        
    for i in range(1, n+1):
        l = []
        for j in range(i):
            l.append('*')
        for j in range(2*(n-i)):
            l.append('b')
        for j in range(i):
            l.append('*')
        print(''.join(l))
        
n = int(input())
pattern(n//2)