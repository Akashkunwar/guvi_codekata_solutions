# QID: 75
# 
# Given a string S,count the maximum number of times a character repeated in the string.If no character is repeated print '0'.
# Input Size : 1 <= N <= 100000
# 
# 
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


a = [str(d) for d in str(input())]
def most_frequent(List):
    return max(set(List), key = List.count)
b = most_frequent(a)
print(a.count(b))