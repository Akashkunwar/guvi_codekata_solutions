# QID: 656
# 
# you are given a string made up of parenthesis only.Your task is to check whether parenthesis are balanced or not.If they are balanced print 1 else print 0
# 
# You are given a string ‘s’
# 
# 
# Print 1 for balanced and 0 for imbalanced
# 
# 
# Sample Input : 
# {({})}
# 
# 
# Sample Output : 
# 1
# 


# Solution:


n = input()
r = 0
m = 0
for i in n:
    if i in '({[':
        r += 1
    if i in ')}]':
        m += 1
if r == m:
    print(1)
else:
    print(0)