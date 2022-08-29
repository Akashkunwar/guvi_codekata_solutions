# QID: 879
# 
# Write a code to generate the following pattern.
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
# Input consists of a single integer that corresponds to R, the number of rows. R is always an odd number.Where 1<=R<=100.
# 
# Print the character with the letter 'b' pattern with the size based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# *********
# b*******b
# bb*****bb
# bbb***bbb
# bbbb*bbbb
# 


# Solution:


def pattern(n):
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
pattern(n)