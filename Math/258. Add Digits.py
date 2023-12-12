'''
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 
Constraints:

0 <= num <= 231 - 1
'''



def addDigits(num):
    while num >= 10:
        num = sum(int(i) for i in str(num))
    return num
    
print(addDigits(199))





# def addDigits(num):
#     if num == 0:
#         return 0
#     return 1 + (num - 1) % 9
# print(addDigits(199))

'''
199
The process is
199 --> 1+9+9 --> 27
27 --> 2+7 --> 9
Since 9 has only one digit, return it.
So we will output 9.
But according to the problem description, the input should be a non-negative integer num with 0 <= num <= 231


'''