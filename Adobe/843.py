# QID: 843
# 
# Given a string expression examine the correctness of pairs and orders of parantheses using <strong>Stack</strong>.
# If it has pair of parentheses print yes else print no 
# 
# An expression containing various types of Parentheses.
# 
# Print yes or no based on the given input
# 
# Sample Input : 
# {([])}
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