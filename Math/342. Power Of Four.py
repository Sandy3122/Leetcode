'''
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-2^31 <= n <= 2^31 - 1
 

Follow up: Could you solve it without loops/recursion?
'''

import math

# def isPowerOfFour(self, n: int) -> bool:
#     if n == 1:
#         return True
#     if n <= 0 or n % 4:
#         return False
#     return self.isPowerOfFour(n // 4)
    


def isPowerOfFour(n):
    # return n <= 0 or math.log(n, 4) % 1 == 0
    return n > 0 and math.log(n, 4) % 1 == 0
    

print(isPowerOfFour(20)) # False





res = math.log(16, 4)
print(res) # It Gives 2.0

print(16%4)
print(16 & (16 - 1))    # Bitwise