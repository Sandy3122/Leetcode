'''
2427. Number of Common Factors

Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.

Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
 
Constraints:

1 <= a, b <= 1000
'''


def commonFactors(n1, n2):
    result = []
    def factors(num):
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                if num // i != i:
                    # result.append(i)
                    # result.append(num // i)
                    result.extend([i, num // i])
                else:
                    result.append(i)
        return result
    
    n1Factors = set(factors(n1))
    n2Factors = set(factors(n2))
    
    commonFactors = n1Factors.intersection(n2Factors)
    return len(commonFactors)

print(commonFactors(12, 6))