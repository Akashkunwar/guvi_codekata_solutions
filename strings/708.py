# QID: 708
# 
# You are given two string s1 and s2. You have to tell whether these form pair of (strset) A pair of strings is said to be str set if one string is substring of other.
# 
# You are given two strings ‘s1’ and ‘s2’ 
# 
# Print Yes if they form strset and No if they don’t.
# 
# Sample Input : 
# abc ab
# 
# Sample Output : 
# Yes
# 


# Solution:


a,b = input().split(" ")
c = list(range(0,len(b)))
d = []
for x in c:
  d.append(b[x])
e = []
try:
  for x in c:
    e.append(a.index(d[x]))
except:
  pass
if len(e)==len(c):
  print("Yes")
else:
  print("No")