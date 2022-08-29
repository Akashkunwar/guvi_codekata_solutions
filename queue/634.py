# QID: 634
# 
# Joyal was given a sentence. His task is to delete the two words that comes together and print the sentence so that the words in the output sentence have distinct words compared to their adjacent words. If no words are present in the output sentence print -1
# 
# You are given input string 'S'
# 
# Print the all the words that are left in the string 's' so that the words in the output sentence have distinct words compared to their adjacent words. Print -1 if no words are left
# 
# Sample Input : 
# I am john cena cena john
# 
# Sample Output : 
# I am
# 


# Solution:


a = [str(i) for i in input().split(' ')]
k = a.copy()
b = a[1:]

for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
for x,y in zip(a,b):
  if x==y:
    a.remove(x)
    a.remove(x)
    b.remove(x)
    b.remove(x)
if len(a)==0:
  print(-1)
else:
  print(*a)