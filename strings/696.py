# QID: 696
# 
# You are given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S. If you find all the characters are repeating print the answer as -1
# 
# You are given a string ‘s’
# 
# 
# Print the first non occurring character if possible else -1.
# 
# 
# Sample Input : 
# apple
# 
# Sample Output : 
# a
# 


# Solution:


a = input()
b = list(range(0,len(a)))
c = []
for x in b:
  c.append(a[x])
d = []
for x in c:
  d.append(a.count(x))
try:
  b = a[d.index(1)]
except:
  b = -1
print(b)