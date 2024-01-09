'''

20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''


# print(s[0])
# for i in range(0, len(s), 2):
#     # print(s[i])
#     if s[i:i+2] == "()" or s[i:i+2] == "{}" or s[i:i+2] == "[]":
#         print("True")
#     else:
#         print("False")


# By using stack data structure

s = "(){}[{[{{()}}]}]"

def isValid(s):
    stack = []  # Creating an empty stack

    # Iterate through each character in the string
    for i in s:
        if i in "({[":
            stack.append(i) # If it's an opening bracket, push onto the stack
            # print("stack:", stack)
        else:
            # If the stack is empty
            if not stack:
                return False

            # Pop the top element from the stack  
            top = stack.pop()
            # print("top:", top)

             # Check if the current closing bracket matches the corresponding opening bracket
            if (i == ")" and top != "(") or (i == "}" and top != "{") or (i == "]" and top != "["):
                return False

    return not stack

res = isValid(s)
print(res)
