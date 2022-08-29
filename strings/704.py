# QID: 704
# 
# You are given two strings . Your task is to tell whether the pair of strings is panagram.
# 
# A pair of strings are said to be panagram if they both are palindrome and are anagram of each other.
# 
# You will be given two strings ‘s1’ and ‘s2’
# 
# 
# Print 1 if they are panagram and 0 if they are not
# 
# 
# Sample Input : 
# nitin intni
# 
# 
# Sample Output : 
# 1
# 


# Solution:


z = []
def panagram(a):
  b = len(a)
  if b%2!=0:
    c = int((b+1)/2)
    r = list(range(c,b))
    l = list(range(c-2,-1,-1))
    d = []
    e = []
    for x in r:
      d.append(a[x])
    for y in l:
      e.append(a[y])
  elif b%2==0:
    b = len(a)
    c = int(b/2)
    r = list(range(c,b))
    l = list(range(c-1,-1,-1))
    b = 0
    d = []
    e = []
    for x in r:
      d.append(a[x])
    for y in l:
      e.append(a[y])
  else:
    pass
  if d==e:
    z.append(1)
  else:
    z.append(0)

t,k = input().split(" ")
panagram(t)
panagram(k)
if (z[0] == 1 & z[1] == 1):
  print(1)
else:
  print(0)