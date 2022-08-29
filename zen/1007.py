# QID: 1007
# 
# Given a string remove special characters if there is no special characters print -1
# 
# Given a string
# 
# Print the string  or -1
# 
# Sample Input : 
# Xyz-aBc-nMk
# 
# Sample Output : 
# XyzaBcnMk
# 


# Solution:


a = input()
b = ''
for x in a:
    if x!='-':
        b=b+x
    else:
        pass
if a==b:
    print(-1)
else:
    print(b)