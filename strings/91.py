# QID: 91
# 
# Given a string S consisting of only '(' and ')', print 'yes' if it is balanced otherwise print 'no'.
# 
# 
# Sample Testcase :
# INPUT
# (())
# OUTPUT
# yes
# 
# 
# 
# 


# Solution:


open_list = ["[","{","("]
close_list = ["]","}",")"]
def check(myStr):
	stack = []
	for i in myStr:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				print("no")
	if len(stack) == 0:
		print("yes")
	else:
		print("no")
string = input()
check(string)