#  Program for creating a machine which count number of 1’s and 0’s in a given string
# By - Mayank Singh
# Date of Creation - 04-12-2021
# Last Modified - 04-12-2021

myinput = input("Enter a string of 0's & 1's: ")

count0 = 0
count1 = 0
for i in myinput:
    if i=="0":
        count0 += 1
    if i=="1":
        count1 += 1

print("Total no. of 0's are:", count0)
print("Total no. of 1's are:", count1)
    
# Output
# Enter a string of 0's & 1's: 110110
# Total no. of 0's are: 2
# Total no. of 1's are: 4
# Enter a string of 0's & 1's: 00110
# Total no. of 0's are: 3
# Total no. of 1's are: 2