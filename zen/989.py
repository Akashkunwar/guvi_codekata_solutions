# QID: 989
# 
# Given a number n followed by n numbers Remove  repeating numbers
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the numbers which is non- repeating numbers
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 5 7 6 8
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
b = []
for x in a:
  if a.count(x)==1:
    b.append(x)
  else:
    pass
print(*b)