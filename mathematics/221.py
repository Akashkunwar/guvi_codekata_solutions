# QID: 221
# 
# The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.For the given input string(S) and shift print the encrypted string.
# 
# 
# Sample Testcase :
# INPUT
# ABCdEFGHIJKLMNOPQRSTUVWXYz 23
# OUTPUT
# XYZaBCDEFGHIJKLMNOPQRSTUVw
# 
# 
# 
# 


# Solution:


def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result
text,s1 = map(str, input().split(" "))
s = int(s1)
print (encrypt(text,s))