# QID: 550
# 
# You are given a series 3, 20, 63, 144, 275… . Go through the series in order to find the answer.You are given with a number n. Find the nth number of series.
# 
# You are given a number ‘n’
# 
# 
# Print the nth number of series.
# 
# 
# Sample Input : 
# 4
# 
# Sample Output : 
# 144
# 


# Solution:


a = []
b = []
aa = int(input())
for x in range(1,aa+1):
  a.append(x**2)
for x in range(3,aa*2+2,2):
  b.append(x)
c = []
for x,y in zip(a,b):
  c.append(x*y)
print(c[-1])