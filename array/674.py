# QID: 674
# 
# You are given with string of words,we have to arrange them in reverse saturated order.
# 
# You are given a string ‘s’.
# 
# Print the reverse saturated order
# 
# Sample Input : 
# I am kohli fan
# 
# Sample Output : 
# I ma ilhok naf
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
	aa = reverserWords(string)