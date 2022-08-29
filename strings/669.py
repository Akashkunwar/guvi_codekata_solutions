# QID: 669
# 
# Rahul is given a task to manipulate a string, He hired you as a developer your task is to delete all the repeating characters and print the result left.
# 
# You are given a string ‘s’
# 
# Print the remaining string
# 
# Sample Input : 
# mississipie
# 
# Sample Output : 
# mpe
# 


# Solution:


a = list(input())
b = []
for x in a:
  b.append(a.count(x))
t = -1
g = []
for x in b:
  t = t+1
  if x==1:
    g.append(a[t])
print(*g,sep='')