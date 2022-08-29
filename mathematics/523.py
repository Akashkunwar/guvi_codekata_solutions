# QID: 523
# 
# A stiff number is a number which can only be formed by sum of two number which are co prime. You are given with a number (n). Write a programme to determine whether a number is stiff or not
# 
# You are given a number n
# 
# 
# Print Stiff or not stiff
# 
# 
# Sample Input : 
# 9
# 
# Sample Output : 
# Stiff
# 
# 


# Solution:


a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
b = int(input())
c = 0
for x in a:
  for j in a:
    if x+j==b:
      c = c + 1
      break
    else:
      pass
if c>1:
  print('Stiff')
else:
  print('not stiff')