'''
1175. Prime Arrangements

Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100
'''



# def numPrimeArrangement(num):
#     def isPrime(n):
#         if n < 2:
#             return False
#         for i in range(2, int((n**0.5)) + 1):   # For Square Root : n**0.5
#             if n % i  == 0:
#                 return False
#         return True
#     count_prime = sum([isPrime(i) for i in range(1, num+1)])
#     print(count_prime)
#     factorial = 1
#     for i in range(1, count_prime + 1):
#         factorial *= i 
#     # print("factorial", factorial)

#     nonPrime = (num - count_prime)
#     # print("nonPrime", nonPrime)
#     nonPrimeFactorial = 1
#     for i in range(1, nonPrime + 1):
#         nonPrimeFactorial *= i
#     # print("nonPrimeFactorial", nonPrimeFactorial)

#     res = (factorial * nonPrimeFactorial) % (10 ** 9 +7)
#     return res

# print(numPrimeArrangement(5))






def numPrimeArrangements(n):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def factorial(num):
        res = 1
        for i in range(1, num + 1):
            res = (res * i) % (10**9 + 7)
        return res
    
    countPrimes = sum([isPrime(i) for i in range(1, n+1)])
    nonPrimes = n - countPrimes
    permutationsOfPrimes = factorial(countPrimes)   
    permutationsOfNonPrimes = factorial(nonPrimes)

    return (permutationsOfPrimes * permutationsOfNonPrimes) % (10 ** 9 +7)

print(numPrimeArrangements(8))
print(numPrimeArrangements(5))

