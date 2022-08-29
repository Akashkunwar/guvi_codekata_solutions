# QID: 629
# 
# You are given a string of different type of brackets. Your task is to check whether the given string is balanced or not balanced.
# A string is said to be balanced if the number of opening brackets are equal to the number of closing brackets where the brackets should be of same kind.
# 
# You are given a string ‘s’.
# 
# 
# Print 'yes' if the given string is balanced and no if it is not
# 
# 
# Sample Input : 
# {}(())[][][{}]
# 
# 
# Sample Output : 
# yes
# 


# Solution:


def areBracketsBalanced(expr):
	stack = []
	for char in expr:
		if char in ["(", "{", "["]:
			stack.append(char)
		else:
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False
	if stack:
		return False
	return True
if __name__ == "__main__":
	expr = input()

	if areBracketsBalanced(expr):
		print("yes")
	else:
		print("no")