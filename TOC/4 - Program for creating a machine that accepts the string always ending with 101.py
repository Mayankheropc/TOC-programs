# Program for creating a machine that accepts the string always ending with 101.
# By - Mayank Singh
# Date of Creation - 04-12-2021
# Last Modified - 04-12-2021

myinput = input("Enter a string of 0 & 1: ")

if len(myinput)<3:
    print("Not Accepted (string length is too small)")

elif len(myinput)==3:
    if myinput=="101":
        print("Accepted")
    else:
        print("Not Accepted")

else:
    myinput = int(myinput)
    mynum = 0
    for i in range (0,3):
        temp = int(myinput%10)
        mynum = mynum*10 + temp
        myinput = int(myinput/10)
    if mynum == 101:
        print("Accepted")
    else:
        print("Not Accepted")

# Output
# Enter a string of 0 & 1: 11
# Not Accepted (string length is too small)
# Enter a string of 0 & 1: 101
# Accepted
# Enter a string of 0 & 1: 1100101
# Accepted
# Enter a string of 0 & 1: 110010100
# Not Accepted