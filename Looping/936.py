# QID: 936
# 
# Write a code to get 2 integers A and N. Print the integer A, N times in separate line.
# 
# First line contains an integer A.
# Second line contains an Integer N.
# 
# Print the integer A, N times in a separate line. 
# 
# Sample Input : 
# 2 3
# 
# Sample Output : 
# 2
# 2
# 2
# 


# Solution:


m, n = map(int, input().split())
for line in range(n):
  print(m)