# QID: 576
# 
# Assume you are john. John has one younger sister jenny. He wants to gift her some toys. He has a price list of toys and he has some amount on hand. Your task is to tell him how many toys john will be able to buy for her sister
# 
# First line contains two integer ‘n’ and ‘k’ ,n denotes the number of toys and k denotes total money he has.Next line contains n space separated integers denoting price of each toy
# 
# 
# Print the max number of toys he can buy.
# 
# 
# Sample Input : 
# 7 50
# 1 12 5 111 200 1000 10
# 
# 
# Sample Output : 
# 4
# 


# Solution:


b,c = input().split()
c = int(c)
a = [int(i) for i in input().split()]

a.sort()

b = []
for x in a:
  if len(b)==0:
    b.append(x)
  else:
    b.append(b[-1]+x)

d = 0
for x in b:
  if x<c:
    d+=1
  elif x<c:
    d+=1
  else:
    pass
print(d)