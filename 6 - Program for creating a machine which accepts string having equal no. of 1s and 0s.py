# Program for creating a machine which accepts string having equal no. of 1’s and 0’s.
# By - Mayank Singh
# Date of Creation - 04-12-2021
# Last Modified - 04-12-2021

myinput = input("Enter a string of 0's & 1's: ")

if len(myinput)<2:
    print("Not Accepted string length is too small")
else:
    count0 = 0
    count1 = 0
    for i in myinput:
        if i=="0":
            count0 += 1
        if i=="1":
            count1 += 1
    
    if count0 == count1:
        print("Accepted")
    else:
        print("Not Accepted")

# Output
# Enter a string of 0's & 1's: 1
# Not Accepted string length is too small
# Enter a string of 0's & 1's: 11011000
# Accepted
# Enter a string of 0's & 1's: 11100
# Not Accepted
# Enter a string of 0's & 1's: 1011
# Not Accepted