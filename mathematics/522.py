# QID: 522
# 
# You are given a task to tell whether the number is pure or not. A pure number is a number whose sum of digits is multiple of 3.
# 
# O(1) time and O(1) space
# 
# You are given a number n.
# 
# 
# Print yes if it is pure else not
# 
# 
# Sample Input : 
# 13
# 
# 
# Sample Output : 
# not
# 
# 


# Solution:


a = input()
r = 0
for i in a:
    r += int(i)
if r % 3 == 0:
    print('yes')
else:
    print('not')