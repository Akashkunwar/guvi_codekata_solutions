# QID: 681
# 
# Nishant is a short heighted person. He is standing facing N pillars of different heights with ith pillar having height hi. He tries to see all the possible pillars. He wants to know that how many buildings will he be able to see in the range.
# 
# First line contains input ‘n’ denoting size of array.Next line contains n space separated numbers
# 
# Print the maximum towers he can see
# 
# Sample Input : 
# 5
# 11 5 9 6 7
# 
# 
# Sample Output : 
# 1
# 


# Solution:


aa = int(input())
b = []
a = [int(i) for i in input().split()]
for x in a:
  if x<=aa:
    b.append(x)
  else:
    pass
print(len(b))