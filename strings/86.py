# QID: 86
# 
# Given a sentence S take out the extra spaces.If no extra space is present print the same as output.
# Input Size : |s| <= 100000(complexity O(n))
# 
# 
# Sample Testcase :
# INPUT
# codekata    challenge
# OUTPUT
# codekata challenge
# 
# 
# 
# 


# Solution:


a = [str(i) for i in input().split(" ")]

b = []
for x in a:
  if x != '':
    b.append(x)

print(*b)