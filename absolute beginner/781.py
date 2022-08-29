# QID: 781
# 
# Using the method of looping, write a program to print the table of 9 till N in the format as follows:
# 
# (N is input by the user)
# 
# 9 18 27...
# 
# Print NULL if 0 is input
# 
# A positive integer is provided as an input.
# 
# Print the table of nine with single space between the elements till the number that is input.
# 
# Sample Input : 
# 3
# 
# Sample Output : 
# 9 18 27
# 


# Solution:


x = int(input())
if x > 0:
    count = 1
    a = []
    while count<=x:
        z = 9*count
        a.append(z)
        #print(z, end=" ")
        count += 1
else:
    print("NULL")
b = str(a)[1:-1]
c = b.replace(',',"")
print(c)