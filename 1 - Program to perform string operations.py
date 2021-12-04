# Program to perform string operations
# By - Mayank Singh
# Date of Creation - 04-12-2021
# Last Modified - 04-12-2021

string1 = input("Enter first name: ")
string2 = input("Enter last name: ")

# combining these 2 strings
finalstr = string1 + " " + string2
print("Full name is:", finalstr)

# Total no. of characters including space
print("Total no. of characters including space:", len(finalstr))

# converting to Upper Case
print("Full name in UPPERCASE is:", finalstr.upper())

# converting to Lower Case
print("Full name in lowercase is:", finalstr.lower())

# combining string without space
finalstr = string1 + string2
print("Full name without space:", finalstr)

# Total no. of characters without including space
print("Total no. of characters including space:", len(finalstr))

# Output
# Enter first name: Mayank
# Enter last name: Singh
# Full name is: Mayank Singh
# Total no. of characters including space: 12
# Full name in UPPERCASE is: MAYANK SINGH
# Full name in lowercase is: mayank singh
# Full name without space: MayankSingh
# Total no. of characters including space: 11
