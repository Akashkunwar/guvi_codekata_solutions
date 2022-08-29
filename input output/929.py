# QID: 929
# 
# Write a code to get the input in the given format and print the output in the given format
# 
# First-line indicates two integers separated by space. Second-line indicates three integers separated by space. Third-line indicates three integers separated by space
# 
# Print the input in the same format.
# 
# Sample Input : 
# 2 5
# 2 5 6
# 2 4 5
# 
# Sample Output : 
# 2 5
# 2 5 6
# 2 4 5
# 


# Solution:


p,r = map(int, input().split(" "))
a,b,c = map(int, input().split(" "))
d,e,f = map(int, input().split(" "))
print(p,r)
print(a,b,c)
print(d,e,f)