# QID: 476
# 
# You are given with two integers denoting h and m. Your task is to find the angle between that particular min hand and hour hand.
# 
# First line contains two numbers h and n.
# 
# Print the angle form by the min pointer and hour pointer
# 
# Sample Input : 
# 3 30
# 
# Sample Output : 
# 75
# 


# Solution:


a,b = input().split()
a = int(a)
b = int(b)
aaa = .5*b
aa = a*30 + aaa
aa = int(aa)
bb = b*6
if aa>bb:
  d = aa-bb
  if d==360:
    print(0)
  else:
    print(360-d)
else:
  e = bb-aa
  if e==360:
    print(0)
  else:
    print(e)