# Program for creating machine that accept three consecutive one.
# By - Mayank Singh
# Date of Creation - 04-12-2021
# Last Modified - 04-12-2021

myinput = input("Enter a string of 0 & 1: ")
if len(myinput)<3:
    print("Not Accepted (string length is too small)")

elif len(myinput)==3:
    if myinput=="111":
        print("Accepted")
    else:
        print("Not Accepted")

else:
    count1 = 0
    for i in myinput:
        if count1 == 3:
            break
        if i == "1":
            count1 +=1
        else:
            count1 = 0

    if count1 == 3:
        print("Accepted")
    else:
        print("Not Accepted")


# Output
# Enter a string of 0 & 1: 10
# Not Accepted (string length is too small)
# Enter a string of 0 & 1: 100
# Not Accepted
# Enter a string of 0 & 1: 10011100
# Accepted
# Enter a string of 0 & 1: 0110010011
# Not Accepted