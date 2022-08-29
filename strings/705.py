# QID: 705
# 
# You are given a string s.Print all the duplicate characters of string.
# 
# String ‘s; is given
# 
# 
# Print only duplicate character and -1 if no character is duplicate.
# 
# 
# Sample Input : 
# abcddee
# 
# 
# Sample Output : 
# d e
# 
# 


# Solution:


import pandas as pd
b = list(input())
d = []
for x in b:
  d.append(b.count(x))
e = pd.DataFrame(b,d)
f = list(set(list(e[e.index>1][0])))
if len(f)==0:
  print(-1)
else:
  print(*f)