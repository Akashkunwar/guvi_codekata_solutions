# QID: 106
# 
# Given an angle A, print the sine of the given angle.
# 
# 
# Sample Testcase :
# INPUT
# 30
# OUTPUT
# 0.5
# 
# 
# 
# 


# Solution:


import math
angle_in_degrees = int(input())
angle_in_radians = math.radians(angle_in_degrees)
sin_of_angle = math.sin(angle_in_radians)
print(float(format(sin_of_angle,'.1f')))