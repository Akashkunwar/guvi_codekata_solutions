# QID: 775
# 
# You are given with a number <strong>A</strong> i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit. 
# 
# <em>Note: In case of decimal values, round-off to <strong>two</strong> decimal places.</em>
# 
# A number is provided in Celcius as the input of the program.
# 
# The output shall be the temperature converted into Fahrenheit corresponding to the input value print up to two decimal places and round off if required.
# 
# Sample Input : 
# 12
# 
# Sample Output : 
# 53.60
# 


# Solution:


a = int(input())
b = a*9/5+32
print(round(b,2))