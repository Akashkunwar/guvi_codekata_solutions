# QID: 512
# 
# You are a software engineer at an MNC. You are given the task of sorting the employees in your company based on their salary. Perform the task so that the employees, including yourself, will get a bonus from the management.
# 
# CONSTRAINT:
# 
# 0<=salary<=1000000
# 
#  
# 
# Number of employees followed by their name and salary
# 
# 
# Sorted list of employee names
# 
# 
# Sample Input : 
# 3
# Karthik 23000 rohan 81734 varshini 12343
# 
# Sample Output : 
# varshini
# Karthik
# Rohan
# 


# Solution:


aa = input()
a = [str(i) for i in input().split()]
b = []
c = []
for x in a:
  if x.isalpha():
    b.append(x)
  elif x.isdigit():
      c.append(int(x))
  else:
    pass
dic = dict(zip(b,c))
sorted_dt = {key: value for key, value in sorted(dic.items(), key=lambda item: item[1])}
d = list(sorted_dt.keys())
for x in d:
  print(x)