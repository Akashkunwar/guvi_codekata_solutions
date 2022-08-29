# QID: 37
# 
# Given a string 'S' and a character 'K', find at what position the character 'K' occurs for the first time in 'S'.(Assume the index of string starts at 1).If the character is not found in 'S' then print -1
# Input Size : |s| <= 100000
# 
# 
# Sample Testcase :
# INPUT
# codekata a
# OUTPUT
# 6
# 
# 
# 
# 


# Solution:


a,b = input().split()
if b in a:
    print(a.index(b)+1)
else:
    print(-1)