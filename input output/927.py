# QID: 927
# 
# Write a code to get the input in the given format and print the output in the given format.
# 
# First-line indicates two integers which are the size of array and 'K' value.
# Second-line indicates an integer contains elements of an array.
# 
# Print the taken input in the same format.
# 
# Sample Input : 
# 5 3
# 1 2 3 4 5
# 
# Sample Output : 
# 5 3
# 1 2 3 4 5
# 


# Solution:


a1 = [int(i) for i in input().split(" ")]
a2 = [int(i) for i in input().split(" ")]
print(*a1, sep = " ")
print(*a2, sep = " ")