# QID: 938
# 
# Write a code to get an integer N and print the even values from 1 till N in a separate line.
# 
# A single line contains an integer N.
# 
# Print the even values from 1 to N in a separate line.
# 
# Sample Input : 
# 6
# 
# Sample Output : 
# 2
# 4
# 6
# 


# Solution:


n=int(input())
m = n+1
for x in range(2,m,2):
  print(x)