# QID: 247
# 
# Given a string S of length N, write a program that would reverse every word in the string.
# Input Size : 1 <= N <= 100000
# Sample Testcases :
# INPUT
# Hello World
# OUTPUT
# olleH dlroW
# 
# 
# 
# 


# Solution:


def reverserWords(string):
	st = list()
	for i in range(len(string)):
		if string[i] != " ":
			st.append(string[i])
		else:
			while len(st) > 0:
				print(st[-1], end= "")
				st.pop()
			print(end = " ")
	while len(st) > 0:
		print(st[-1], end = "")
		st.pop()

if __name__ == "__main__":
	string = input()
	reverserWords(string)