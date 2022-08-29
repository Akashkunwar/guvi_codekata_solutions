# QID: 882
# 
# Generate the aplhabet pattern using nested loops.
# 
# Input consists of a string S.where length of the string (S) Where 2<=S<=20.
# 
# Print the alphabet pattern from the given input string S.
# 
# Sample Input : 
# abcdef
# 
# Sample Output : 
# abcdef
# b    e
# c    d
# d    c
# e    b
# fedcba
# 


# Solution:


def pattern(s):
    n = len(s)
    print(s)
    for i in range(1, n-1):
        res = s[i]
        res += ' '*(n-2)
        res += s[n-i-1]
        print(res)
    print(s[::-1])
    
s = input()
pattern(s)