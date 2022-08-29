# QID: 934
# 
# Write a code to get the input in the given format and print the output in the given format.
# 
# A single line contains a string.
# 
# Print the characters in a string separated by comma.
# 
# 
# Sample Input : 
# guvi
# 
# Sample Output : 
# g,u,v,i
# 


# Solution:


a = [str(d) for d in str(input())]
print(*a, sep = ",")