# QID: 707
# 
# You are given a string s. Your task is to print the characters which are not repeated with a single space in between the characters.
# 
# You are given a string ‘s’.
# 
# 
# Print the characters present once and -1 if there is no character which satisfy above condition
# 
# 
# 
# Sample Input : 
# dabbc
# 
# 
# Sample Output : 
# d a c
# 
# 


# Solution:


import pandas as pd
b = list(input())
d = []
for x in b:
  d.append(b.count(x))
e = pd.DataFrame(b,d)
f = list(e[e.index==1][0])
if len(f)==0:
  print(-1)
else:
  print(*f)