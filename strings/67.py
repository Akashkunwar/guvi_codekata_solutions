# QID: 67
# 
# Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
# Input Size : |s| <= 10000000(complexity O(n))
# 
# 
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# ocedakat
# 
# 
# 
# 


# Solution:


a = input()
output = ''
i = 0
while i < len(a):
        if i + 1 < len(a):
                output = output + a[i + 1]
                output = output + a[i]
        i = i + 2
print(output)