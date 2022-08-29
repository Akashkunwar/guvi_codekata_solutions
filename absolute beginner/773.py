# QID: 773
# 
# You are provided with a number, &quot;<strong>N</strong>&quot;. Find its factorial.
# 
# A positive integer is provided as an input.
# 
# Print the factorial of the integer.
# 
# Sample Input : 
# 2
# 
# Sample Output : 
# 2
# 


# Solution:


import numpy as np
n = int(input())
print(np.prod(range(1,n+1)))