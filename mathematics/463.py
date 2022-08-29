# QID: 463
# 
# You are given an integer N, find if the number is divisible by 4.
# 
# N >= 1
# 
# 1 <= No. of digits in N <= 1000
# 
#  
# 
#  
# 
#  
# 
#  
# 
# Read an integer N
# 
# Print YES if N is divisible by 4, NO otherwise.
# 
# Sample Input : 
# 64
# 
# Sample Output : 
# YES
# 


# Solution:


a = int(input())
if a%4==0:
  print('YES')
else:
  print('NO')