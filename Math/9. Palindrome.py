'''
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''


# def palindrome(x):
#     # Convert the number into string for easy manipulation
#     if x < 0:
#         return False
#     dup = x
#     revNum = int(str(x)[::-1])
#     if revNum == dup:
#        return True
#     else:
#         return False
    
# print(palindrome(-121))




# # Using Math
# def isPalindrome(x):
#     # Handling negative numbers
#     if x < 0:
#         return False
#     dup = x
#     reversed_num = 0
    
#     while x > 0:
#         digit = x % 10
#         x //= 10
#         reversed_num = reversed_num * 10 + digit
    
#     return dup == reversed_num



# Best Approach
def isPalindrome(x):
    return str(x) == str(x)[::-1]


print(isPalindrome(-121))