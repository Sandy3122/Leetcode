'''
2544. Alternating Digit Sum

You are given a positive integer n. Each digit of n has a sign according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.

Example 1:

Input: n = 521
Output: 4
Explanation: (+5) + (-2) + (+1) = 4.
Example 2:

Input: n = 111
Output: 1
Explanation: (+1) + (-1) + (+1) = 1.
Example 3:

Input: n = 886996
Output: 0
Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
 
Constraints:

1 <= n <= 109

'''



# def alternateDigitSum(n):
#     # Convert number into string for easy access and manipulation
#     strNum = str(n)
#     # Initialize result variable
#     resPositive = 0
#     resNegative = 0
#     # Iterate through each character in the string
#     for i in strNum:
#         if int(i) % 2 == 0:
#             resPositive = int(i) - resPositive
#             print("Positive", resPositive)
#         else:
#             resNegative = int(i) + resNegative
#             print("Negative", resNegative)
#     return (resPositive - resNegative) if resPositive > resNegative else (resNegative - resPositive)

# print(alternateDigitSum(111))



# def alternateDigitSum(n):
#     temp = 1
#     count = sum(str(n))


# This Method Exceeds The Time Limit

def alternateDigitSum(n):
    sum = 0
    res = str(n)
    for i in range(len(res)):
        if i % 2 == 0:
            sum = sum + int(res[i])
        else:
            sum = sum - int(res[i])    
    return sum
print(alternateDigitSum(10))

# Time Complexity O(n)