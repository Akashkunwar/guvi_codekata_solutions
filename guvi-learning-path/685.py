# QID: 685
# 
# Aditi is fond of strings.she heard about Lcs for two strings.Now she wants to try this for 3 strings.But in between she got confused now, your task is to help her.You are given exactly 3 strings.
# 
# Develop an algorithm which to find lcs for 3 strings.
# 
# You are given 3 strings.
# 
# Print the lcs of 3 string or print -1 if there is no lcs between 3 strings
# 
# Sample Input : 
# Guvi yuvi yuvirat
# 
# Sample Output : 
# uvi
# 


# Solution:


aa = [i for i in input().split()]
a = aa[0] 
b = aa[1] 
c = aa[2]
d = ''
for i in a:
  if i in b and not i in d:
    d+=i
e = ''
for i in d:
  if i in c and not i in e:
    e+=i
if len(e)>0:
    print(e)
else:
    print(-1)