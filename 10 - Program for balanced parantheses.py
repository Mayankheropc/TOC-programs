# Python3 program to check for balanced brackets.
# By - Mayank Singh
# Date of Creation - 04-12-2021
# Last Modified - 04-12-2021

# function to check if brackets are balanced
def areBracketsBalanced(expr):
	stack = []
	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:
			# Push the element in the stack
			stack.append(char)
		else:
			# IF current character is not opening
			# bracket, then it must be closing.
			# So stack cannot be empty at this point.
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
	# Check Empty Stack
	if stack:
		return False
	return True
# Driver Code
expr = input("Enter string of parantheses: ")
# Function call
if areBracketsBalanced(expr):
	print("Balanced")
else:
	print("Not Balanced")
# Output
# Enter string of parantheses: ({[]})
# Balanced
# Enter string of parantheses: {}(){()}
# Balanced
# Enter string of parantheses: {{(}]
# Not Balanced
