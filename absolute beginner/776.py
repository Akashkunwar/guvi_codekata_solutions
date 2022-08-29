# QID: 776
# 
# You are provided with the radius of a circle &quot;A&quot;. Find the length of its circumference.
# 
# <em>Note: In case the output is coming in decimal, roundoff to 2nd decimal place. In case the input is a negative number, print &quot;Error&quot;.</em>
# 
# The Radius of a circle is provided as the input of the program.
# 
# Calculate and print the Circumference of the circle corresponding to the input radius up to two decimal places.
# 
# Sample Input : 
# 2
# 
# Sample Output : 
# 12.57
# 


# Solution:


a = float(input())
c = 2*22/7*a
limited_float = round(c, 2)
print(limited_float)