# QID: 648
# 
#  You are given a string. You have to print &ldquo;Wonder&rdquo; if the string is wonderful and -1 if it is not. A wonderful string is a string,which is made up of exactly 3 different characters.
# 
# You are given a string
# 
# 
# Print “Wonder” if it is wonderful and -1 if it is not
# 
# 
# Sample Input : 
# aabbcc
# 
# 
# Sample Output : 
# Wonder
# 


# Solution:


a = input()
j = 0
r = 1
x = a[j]
for i in a:
    if i == x:
        continue
    else:
        r += 1
        x = i 
if r == 3:
    print('Wonder')
else:
    print(-1)