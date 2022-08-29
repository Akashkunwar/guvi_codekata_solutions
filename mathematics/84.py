# QID: 84
# 
# Given a string S.Validate if a given string is numeric.print 'yes' if it is a numeric otherwise print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# guvigeeks
# OUTPUT
# no
# 
# 
# 
# 


# Solution:


def isNumber(s):
	for i in range(len(s)):
		if s[i].isdigit() != True:
			return False
	return True
if __name__ == "__main__":
	str = input()
	if isNumber(str):
		print("yes")
	else:
		print("no")