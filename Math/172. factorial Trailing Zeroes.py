'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
'''


def trailingZeroes(n):
    # count how many times 2 and 5 are used to make up n!
    ans = 0
    y = 5
    while y <= n:
        ans = ans + (n//y)
        y *= 5
    if n < 0:
        return 0
    return ans


print(trailingZeroes(3))