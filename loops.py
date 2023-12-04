#if for while
# a="hello2"
# if a=="hello" :
#     print(a)
# elif a=="hello1":
#     print("in elif")
# elif a=="hello2":
#     print("in second elif")
# else:
#     print("in else")

#for loop
# l=[1,2,3,54,5]
# for i in l:
#     print(i)
# for i in range(9,1,-1):
#     print(i)

#while
# i=3
# while i:
#     print(i)
#     i-=1

#continue statement
# for i in [3,2,4,5,5,6,7]:
#     print("in main loop",i)
#     if i>=5:
#         print("exiting of loop")
#         continue
#     for j in [5,8,6,2,2,1]:
#         print(j)
        

# print("UpperCase Alphabets :")
# for i in range(ord('A'), ord('Z') + 1):
#     print(chr(i), end=' ')
# print()

# print("LowerCase Alphabets :")
# for i in range(97, 122 + 1):
#     print(chr(i), end=' ')

# print()
# print("LowerCase Alphabets Rever Order :")
# for i in range(122, 96, -1):
#     print(chr(i), end=' ')




# Write a program to count the number of alphabets and number of digits in the string.
# from collections import Counter
# c=Counter(a)
alphCount, string = 0, "Sandeep1234"
# print(c)
for i in range(ord('A'), ord('z') + 1):
    if chr(i) in string:
        alphCount+= string.count(chr(i))
        
print("No.of alphabets :", alphCount)
print("No.of digits :", len(string)-alphCount)




