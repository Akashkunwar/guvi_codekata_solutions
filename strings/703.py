# QID: 703
# 
# You are given a string s.Your task is to print the string in the order they are present and then sum of digits.
# 
# You are given a string ‘s’.
# 
# Print the string and then at last sum of all the digits
# 
# Sample Input : 
# AC30BD40
# 
# 
# Sample Output : 
# ACBD7
# 


# Solution:


a = input()
r = 0
arr = []
for i in a:
    if i in '1234567890':
        r += int(i)
    else:
        print(i, end='')
print(r)