# QID: 942
# 
# Write a code get an integer number as input and print the sum of the digits.
# 
# A single line containing an integer.
# 
# Print  the sum of the digits of the integer.
# 
# Sample Input : 
# 124
# 
# Sample Output : 
# 7
# 


# Solution:


a = int(input())
b = str(a)
c = []
for x in b:
  c.append(x)
d = map(int,c)
d = list(d)
print(sum(d))