# QID: 769
# 
# You are given the coefficients of a quadratic equation in order A, B &amp; C.
# 
# Where A is the coefficient of X<sup>2</sup>,  B is the coefficient of X and C is the constant term in the most simplified form.
# 
# Example: For  X<sup>2</sup> + 5X + 6 = 0, you are given the input as: 1 5 6.
# 
# Write a program to find all of the roots of the quadratic.
# 
# Note: The output should be up to 2nd decimal place (round off if needed) and in case of a recurring decimal use braces i.e. for eg: 0.33333..... => 0.33.
# 
# Note: Use Shri Dharacharya&#39;s Method to solve i.e. X = {-b + &radic;(b&sup2; - 4ac) } / 2a &amp; {-b-&radic;(b&sup2; -4ac)} / 2a
# 
# Three numbers corresponding to the coefficients of x(squared), x and constant are given as an input in that particular order
# 
# Print the two values of X after rounding off to 2 decimal places if required.
# 
# Sample Input : 
# 1 5 6
# 
# Sample Output : 
# -2.00
# -3.00
# 


# Solution:


import cmath

a,b,c=map(int,input().split(" "))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)


print("{:.2f}".format(sol2.real))
print("{:.2f}".format(sol1.real))