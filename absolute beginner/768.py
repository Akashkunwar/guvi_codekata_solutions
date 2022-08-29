# QID: 768
# 
# Let &quot;<strong><em>A</em></strong><em>&quot;</em> be a year, write a program to check whether this year is a leap year or not.
# 
# <em>Print &quot;<strong>Y</strong>&quot; if its a leap year and &quot;<strong>N</strong>&quot; if its a common year.</em>
# 
# A Year is the input in the form of a positive integer.
# 
# Print "Y" if its a leap year and "N" if its a common year.
# 
# Sample Input : 
# 2020
# 
# Sample Output : 
# Y
# 


# Solution:


year = int(input())
if year % 4 == 0 and year % 100 != 0:
    print("Y")
elif year % 100 == 0:
    print("N")
elif year % 400 ==0:
    print("Y")
else:
    print("N")