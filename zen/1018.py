# QID: 1018
# 
#  Given a numbers n and m followed by n*m numbers in matrix format print the sum of the elements in the matrix the element which is even number
# 
# You will given a number n and m followed by n*m numbers in matrix format .
# 0<n<100
# 0,m<100
# 
# print the sum of the elements in the matrix the element which is even number
# 
# Sample Input : 
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 
# Sample Output : 
# 20
# 


# Solution:


a,b = input().split()
a = int(a)
b = int(b)
c = []
for x in range(0,a):
  c.append([int(i) for i in input().split()])
d = 0
for x in c:
  for y in x:
    if y%2==0:
      d = d+y
print(d)