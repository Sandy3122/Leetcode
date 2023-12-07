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


# def commonFactors(n1, n2):
#     result = []
#     def factors(num):
#         for i in range(1, num+1):
#             if num % i == 0:
#                 result.append(i)
#         return result
#     n1Factors = factors(n1)
#     n2Factors = factors(n2)
#     count = 0
#     for i in 


class Solution {
    public int factorProduct(int N) {
        final int m = (int) Math.pow(10,9) + 7;
        long prdc = 1;
        int sqrtN = (int) Math.sqrt(N);

        for (int i = 1; i <= sqrtN; i++) {
            if (N % i == 0) {
                prdc = (prdc * i) % m;
                if (N/i == i) {
                    prdc = (prdc * i) % m;
                }
                else {
                    prdc = (prdc * (N / i)) % m;
                }
            }
        }
        return (int) prdc;
    }
}