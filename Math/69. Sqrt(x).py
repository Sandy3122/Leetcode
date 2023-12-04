'''
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1



Square roots
0, 1, 4, 9, 16, 25, 36, 49, 64, 81 

'''
# Brut Force Case

# import math
# def sqrt(n):
#     if n < 2:
#         return n
#     else:
#         return math.floor(n ** 0.5)
# print(sqrt(48))


# Using Binary Search Data Structure
# Time Complexity: O(logN)

def sqrt(n):
    # if n < 2:
    #     return n
    left, right = 0, n
    while left <= right:
        mid =(left + right) // 2
        # print("mid",mid)
        midSqr = mid * mid
        if midSqr == n:
            return mid
        elif midSqr < n:
            left = mid + 1
            # print("left", left)
        else:
            right = mid - 1
            # print("right", right)
    return right

print(sqrt(81))