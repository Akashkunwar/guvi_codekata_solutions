# QID: 694
# 
# You are given a string s. You have to tell whether the string can be arranged in last to first order.A last to first order is order in which if word 1 ends in say(char a) then the other word must start in char a.
# 
# You are given a string ‘s’.
# 
# Print ‘1’ if string can be arranged in last to first sequence and
# 
# Sample Input : 
# Loan avail
# 
# Sample Output : 
# 1
# 


# Solution:


a = [i for i in input().split()]
b = []
for x in a:
  b.append(x.lower())
d = a[1:]
c = b[0]
z = 0
for x in d:
  if c[-1] == x[0]:
    z = z+1
  elif c[0] == x[-1]:
    z = z+1
  else:
    pass
if z > 0:
    print(1)
else:
    print(-1)