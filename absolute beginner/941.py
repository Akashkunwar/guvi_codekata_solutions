# QID: 941
# 
# Write a code to get an integer N and print the digits of the integer.
# 
# A single line contains an integer N.
# 
# Print the digits of the integer in a single line separated by space,
# 
# Sample Input : 
# 348
# 
# Sample Output : 
# 3 4 8
# 


# Solution:


a = int(input())
b = str(a)
c = []
for x in b:
  c.append(x)
d = map(int,c)
d = list(d)
e = ''.join(str(d).split(","))
res = str(e)[1:-1]
print(res)