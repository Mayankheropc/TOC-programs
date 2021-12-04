# Program to increment the given binary number by 1.
# By - Mayank Singh
# Date of Creation - 04-12-2021
# Last Modified - 04-12-2021

# Function to convert Binary number to Decimal number
def binaryToDecimal(n):
    return int(n,2)

# Function to convert Decimal number To Binary number
def decimalToBinary(n):
 
    if(n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n//2)
    print(n%2, end='')
 
# Driver code
myinput = input("Enter the bunary value: ")
decimal_number = binaryToDecimal(myinput)
decimal_number += 1
print("After incrementing by 1: ", end='')
decimalToBinary(decimal_number)

# Output
# Enter the bunary value: 111
# After incrementing by 1: 1000
# Enter the bunary value: 100
# After incrementing by 1: 101