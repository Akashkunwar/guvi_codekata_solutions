# QID: 644
# 
# You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result
# 
# You are given a long string of digits
# 
# Print the desired result print -1 if result length is 0
# 
# Sample Input : 
# 1331
# 
# 
# Sample Output : 
# 11
# 


# Solution:


a = list(input())
b = []
try:
  for x in range(len(a)):
    if a[x]==a[x+1]:
      b.append(a[x+1])
      a.remove(b[0])
      a.remove(b[0])
except:
  pass
print(*a,sep="")