# QID: 766
# 
# The area of an equilateral triangle is &frac14;(&radic;3a<sup>2</sup>) where &quot;<strong>a</strong>&quot; represents a side of the triangle. You are provided with the side &quot;<strong>a</strong>&quot;. Find the area of the equilateral triangle.
# 
# The side of an equilateral triangle is provided as the input.
# 
# Find the area of the equilateral triangle and print the answer up to 2 decimal places after rounding off.
# 
# Sample Input : 
# 20
# 
# Sample Output : 
# 173.21
# 


# Solution:


import math
a = int(input())
b = math.sqrt(3)/4 * (a*a)
print(round(b, 2))