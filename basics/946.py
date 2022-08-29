# QID: 946
# 
# Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.
# 
# A single line containing 2 integers separated by space.
# 
# Print the HCF of the integers.
# 
# Sample Input : 
# 2 3
# 
# Sample Output : 
# 1
# 


# Solution:


a,b = map(int, input().split(" "))
import numpy as np
c = np.gcd(a,b)
print(c)