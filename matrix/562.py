# QID: 562
# 
# Zaheer is a batsman. He plays a cricket match for six overs and attempts 36 balls. After the match, he analyses his performance and wants to know against which bowler he was able to score the maximum. Help Zaheer find out.
# 
#  
# 
# A list of bowlers in the order in which they bowled the overs followed by Zaheer’s runs scored in each of the 36 balls faced.
# 
# 
# Name of the bowler against whom Zaheer scored the maximum.
# 
# 
# Sample Input : 
# Malinga
# Bumrah
# Chahar
# Tahir
# Malinga
# Chahar
# 0 0 0 1 2 0
# 1 0 1 1 4 0
# 4 0 1 1 6 4
# 0 1 1 1 1 0
# 6 6 4 0 4 0
# 1 4 2 2 1 0
# 
# Sample Output : 
# Malinga
# 


# Solution:


a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
a1,a2,a3,a4,a5,a6=map(int,input().split(" "))
b1,b2,b3,b4,b5,b6=map(int,input().split(" "))
c1,c2,c3,c4,c5,c6=map(int,input().split(" "))
d1,d2,d3,d4,d5,d6=map(int,input().split(" "))
e1,e2,e3,e4,e5,e6=map(int,input().split(" "))
f1,f2,f3,f4,f5,f6=map(int,input().split(" "))
a0 = a1+a2+a3+a4+a5+a6
b0 = b1+b2+b3+b4+b5+b6
c0 = c1+c2+c3+c4+c5+c6
d0 = d1+d2+d3+d4+d5+d6
e0 = e1+e2+e3+e4+e5+e6
f0 = f1+f2+f3+f4+f5+f6
over = [a0,b0,c0,d0,e0,f0]
if a0==max(over):
  print(a)
elif b0==max(over):
  print(b)
elif c0==max(over):
  print(c)
elif d0==max(over):
  print(d)
elif e0==max(over):
  print(e)
elif f0==max(over):
  print(f)