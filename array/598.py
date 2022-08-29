# QID: 598
# 
# ou are given with an array of numbers.You have to print the middlemost element until the size of array becomes zero. When n is odd print the (n/2)+1 index(indexing at 1)
# 
# You are given a number ‘n’ denoting the size of array.Next line contains n space separated numbers.
# 
# 
# Print as mentioned above
# 
# 
# Sample Input : 
# 5
# 1 2 3 4 5 
# 
# 
# Sample Output : 
# 3 2 4 1 5
# 
# 


# Solution:


aa = input()
c = []
a = [int(i) for i in input().split()]
while len(a)>0:
  if len(a)%2==0:
    i = len(a)//2
    c.append(a[i-1])
    a.pop(i-1)  
  else:
    ii = len(a)+1
    i = len(a)//2
    c.append(a[i])
    a.pop(i)
print(*c)