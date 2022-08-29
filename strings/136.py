# QID: 136
# 
# Given 2 strings S and X print the word position of X in S.(word count starts from 1).If the given word doesn't exists in S print '-1'.
# Input Size : 1 <= |s|, |x| <= 1000
# 
# 
# Sample Testcase :
# INPUT
# codekata coding challenge
# coding
# OUTPUT
# 2
# 
# 
# 
# 


# Solution:


a = [str(i) for i in input().split(" ")]
b = input()
try:
    print(a.index(b)+1)
except:
    print(-1)