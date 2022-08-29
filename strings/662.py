# QID: 662
# 
# You are given a paragraph.Your task is to print the words that come just after articles.
# 
# You are given a string ‘s’
# 
# 
# print the words that come just after articles and -1 if there are no articles
# 
# 
# Sample Input : 
# The sun rises in the east
# 
# 
# 
# Sample Output : 
# sun east
# 
# 


# Solution:


aa = 'a'
b = 'an'
c = 'the'
a = [str(i).lower() for i in input().split(' ')]
d = []
t = -1
for x in a:
  t = t+1
  if x==aa or x==b or x==c:
    d.append(a[t+1])
if len(d)==0:
  print(-1)
else:
  print(*d)