# QID: 518
# 
# Rajesh is very fond of numbers. With the given positive number(n) ,he has to tell whether a number is lively or not. A lively number is a number which has same frequency of all integers present.
# 
# A integer ‘n’ will be given
# 
# 
# Print 1 if number is lively and 0 if it is not lively.
# 
# 
# Sample Input : 
# 1212
# 
# 
# Sample Output : 
# 1
# 
# 


# Solution:


a = input()
a = list(a)
b = []
for x in a:
  b.append(a.count(x))
c = list(set(b))
if len(c)==1:
  print(1)
else:
  print(0)