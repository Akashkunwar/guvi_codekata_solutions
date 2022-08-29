# QID: 928
# 
# Write a code to get the input in the given format and print the output in the given format
# 
# First-line indicates two integers separated by space. Second-line indicates two integers separated by space. Third-line indicates two integers separated by space.
# 
# Print the input in the same format.
# 
# Sample Input : 
# 2 4
# 2 4
# 2 4
# 
# Sample Output : 
# 2 4
# 2 4
# 2 4
# 


# Solution:


p,r = map(int, input().split(" "))
a,b = map(int, input().split(" "))
c,d = map(int, input().split(" "))
print(p,r)
print(a,b)
print(c,d)