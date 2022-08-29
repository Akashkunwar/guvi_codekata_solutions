# QID: 525
# 
# Rampal is a number in which the sum of last two digits of that number is multiple of 4.Your teacher has given you the task to make a list of rampal numbers.Your task is to tell whether the number is rampal or not.
# 
#  
# 
# Note : if the number is negative than rampal is a number which has sum of first and last digit as multiple of 4  
# 
# First line contains an input n
# 
# 
# Print yes or no
# 
# 
# Sample Input : 
# 20
# 
# 
# 
# Sample Output : 
# no
# 


# Solution:


a = input()
n = len(a)
m = int(a)
r = 0
for i in a[n-2:]:
    r += int(i)
if r%4 == 0:
    print('yes')
else:
    print('no')