# QID: 986
# 
# Given a number n followed by n numbers Print the repeating numbers
# 
# 0<n<100
# Given a number n 
# Followed by n number in next line
# 
# Print the repeating numbers separated by space
# 
# Sample Input : 
# 6
# 5 7 4 4 6 8
# 
# Sample Output : 
# 4
# 


# Solution:


aa = input()
a = [int(i) for i in input().split()]
b = []
for x in a:
  if a.count(x)>1:
    b.append(x)
  else:
    pass
b = list(set(b))
print(*b)