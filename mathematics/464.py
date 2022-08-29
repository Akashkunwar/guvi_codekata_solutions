# QID: 464
# 
# Given an integer N, find if it is divisible by 11
# 
#  
# 
# N >= 1
# 
# 1 <= No. of digits in N <= 1000
# 
# The only line of input contains an integer N
# 
# Print YES if N is divisible by 11, NO otherwise.
# 
# Sample Input : 
# 1331
# 
# Sample Output : 
# YES
# 


# Solution:


n = int(input())
if n%11==0:
  print("YES")
else:
  print("NO")