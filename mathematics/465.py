# QID: 465
# 
# A sequence is given by: 2, 6, 11, 17, 24,....
# 
# The first term is 2.
# 
# Given an integer N, find the Nth term of the sequence.
# 
# 1 <= N <= 10^18
# 
# Since the answer can be very large print it modulo 1,000,000,007 (10^9 + 7)
# 
# The only line of input contains an integer N
# 
# Print the Nth term of the sequence
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 24
# 


# Solution:


a = 2
b = 4
e = 4
c = int(input())
d = [2]
for x in range(c):
  d.append(a+e)
  b = b+1
  e = e+b
print(d[-2])