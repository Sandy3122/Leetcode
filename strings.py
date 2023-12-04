name = "Seeram Sandeep"

print(len(name))

removeSpaces = name.replace(" ", "")

print('After Removing Spaces :', len(removeSpaces))

revName = name[::-1]

revName = removeSpaces[::-1]

print(revName, '\t', removeSpaces)

'''
Input: lolololo
Output: 
The entered string is symmetrical
The entered string is not palindrome
'''
import math

str1 = input("Enter The String : ")
# Find Symmetric
strHalf = math.floor(len(str1) / 2)
revStr = str1[::-1]
if(str1 == strHalf):
    print("Is Symmentric")
else:
    print("Not Symmetirc")
if(revStr == str1):
    print("Is Palindrome")
else:
    print("Not A Palindrome")
