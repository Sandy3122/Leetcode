'''
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''




# It Only works for positive numbers
# def reverse(n):
#     y = 0
#     while n != 0:
#         # rem = n % 10
#         y = y * 10 + n % 10
#         n = n // 10
#     return y
# print(reverse(32))

# It only works for positive numbers
# def reverse(n):
#     strNum = str(n)
#     revNum = strNum[::-1]
#     return revNum
# print(reverse(-32))






'''
Main Solution
Handling all the signs

'''

def reverse(x):
    int_max = 2**31 - 1
    int_min = -2**31

    # Handling the sign
    is_negative = False
    if x < 0:
        is_negative = True
        x = x * -1
    
    # Converting and Reversing the String
    revNum = str(x)[::-1]

    # Convert back to the integer and apply sign if give number is less than 0
    revNum = int(revNum)
    
    if is_negative:
        revNum = revNum * -1
    
    # Checking for overflow or constrains
    if revNum < int_min or revNum > int_max:
        return 0

    return revNum

print(reverse(-32)) 