# QID: 939
# 
# Write a code to get an integer N and print the values from N to 1.
# 
# A single line contains an integer N.
# 
# Print the values from N to 1 in a separate line.
# 
# Sample Input : 
# 10
# 
# Sample Output : 
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 


# Solution:


a = 1
n = int(input())
while n >= a:
  print(n)
  n = n-1