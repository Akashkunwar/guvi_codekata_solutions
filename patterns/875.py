# QID: 875
# 
# Generate a hollow half pyramid pattern using numbers.
# 
# Given an integer R indicates number of rows.Where 1<=R<=100.
# 
# Print the hollow half pyramid pattern using numbers based on the given integer R.
# 
# Sample Input : 
# 5
# 
# Sample Output : 
# 1
# 12
# 1 3
# 1  4
# 12345
# 


# Solution:


n = int(input())
for i in range(1, n+1):
  for j in range(1, i+1):
    if(j == 1 or j == i or i == n):
      print(j, end = "")
    else:
      print(" ", end = "")
  print()