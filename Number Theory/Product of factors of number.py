'''
Given a number N. Calculate the product of all factors of N. Since Answer can be very large,compute the answer modulo 109+7.

Example 1:

Input:
N=6
Output:
36
Explanation:
Factors of 6 are 1,2,3,6.Their product is
(1*2*3*6)%(109+7)=36.


Example 2:

Input:
N=25
Output:
125
Explanation:
The factors of 25 are 1,5 and 25.
So, Their product is (1*5*25)%(109+7)=125.
'''


def factorsProduct(N):
    mod = 10**9 + 7
    product = 1
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            product *= i % mod
            if N // i != i:
                product *= N // i % mod
    return product

print(factorsProduct(25))
