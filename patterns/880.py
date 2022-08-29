# QID: 880
# 
# Generate the following inverted character with star pattern.
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
# Input consists of a single integer that corresponds to R, the number of rows. R is always an odd number.
# where 1<=R<=100.
# 
# Print the inverted character pattern from the given input size R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# bbbb*bbbb
# bbb***bbb
# bb*****bb
# b*******b
# *********
# 


# Solution:


def pattern(n):
    for i in range(1, n+1):
        l = []
        for j in range(n-i):
            l.append('b')
        for j in range(2*(i-1)+1):
            l.append('*')
        for j in range(n-i):
            l.append('b')
        print(''.join(l))

n = int(input())
pattern(n)