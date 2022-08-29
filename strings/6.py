# QID: 6
# 
# Given a string S, print 'yes' if it has a vowel in it else print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


def vowel(s):
    s = str(s)
    s = s.lower()
    vowel = ("a", "e", "i", "o", "u")
    for char in s:
        if char in vowel:
            print("yes")
            break
    else:
        print("no")
a=str(input())
vowel(a)