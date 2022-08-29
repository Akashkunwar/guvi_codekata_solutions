# QID: 984
# 
# Given a number n Find the sum of the digits of number n
# 
# 0<n<1000
# Given number n
# 
# Print the sum of the digits of number n
# 
# Sample Input : 
# 3589
# 
# Sample Output : 
# 25
# 


# Solution:


a = input()
b = 0
for x in a:
  b = b+int(x)
print(b)