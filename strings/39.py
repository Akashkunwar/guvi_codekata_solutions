# QID: 39
# 
# Given a sentence and string S, find how many times S occurs in the given sentence.If S is not found in the sentence print -1
# Input Size : |sentence| <= 1000000(complexity O(n)).
# 
# 
# Sample Testcase :
# INPUT
# I enjoy doing codekata
# codekata
# OUTPUT
# 1
# 
# 
# 
# 


# Solution:


a = input()
b = input()
c = a.count(b)
if c==0:
    print("-1")
else:
    print(c)