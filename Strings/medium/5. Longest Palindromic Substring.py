'''
5. Longest Palindromic Substring

Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''


# Basic Palindrome Problem.
# s = "xabax"
# def checkPalindrome(s):
#     S = s
#     rev = s[::-1]
#     if S == rev:
#         return True
#     else:
#         return False
    
# print(checkPalindrome(s))






def checkPalindrome(s):
    left, right = 0, len(s) - 1
    for i in s:
        if s[left] == s[right]:
            left += 1
            right -= 1 
            return True
        else:
            return False








s = "xabaabax"
print(checkPalindrome(s))