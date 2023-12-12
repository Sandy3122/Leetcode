'''
Problem
Fibonacci numbers have the following form F1=1, F2=1, F3=2 ... Fn=Fn-1 +Fn-2 .

We have an array { a1,a2,...,aN} which contains N elements. We want to find gcd(F{a1},F{a2},F{a3},...,F{aN}).

InputFormat

The first line contains N, where N denotes size of the array. Each of the next N lines contains a number: the i line contains ai.

Output Format

Print a single integer—the remainder of the division of the resulting number by 1000000007.

Constraints

1<=N<=2*10^5

1<=ai<=10^12

Sample Input

3

2

3

5

Sample Output

11

Explanation

F2=1

F3=2

F5=5

gcd(1,2,5)=1

SampleInput

2

3

6

Sample Output

2

Explanation

F3=2

F6=8

gcd(2,8)=2
'''

# import math

# def getFibonacciSeries(n):
#     res = [0, 1]
#     for i in range(2, n + 1):
#         res.append((res[-1] + res[-2]) % 1000000007)
#     return res

# N = int(input())
# array = []
# for _ in range(N):
#     array.append(int(input()))

# max_index = max(array)

# extracted_fib = []
# for num in array:
#     extracted_fib.extend(getFibonacciSeries(num))

# result_gcd = extracted_fib[0]
# for i in range(1, len(extracted_fib)):
#     result_gcd = math.gcd(result_gcd, extracted_fib[i])






import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER a as parameter.
#

# def solve(a):
#     fib_series = [0, 1]
#     for i in range(2, a+1):
#         fib_series.append((fib_series[-1] + fib_series[-2]) % 1000000007)
        
#     gcdResult = fib_series[1]
    
#     for i in range(2, a):
#         gcdResult = math.gcd(gcdResult, fib_series[i])
        
#     return gcdResult


# print(solve(2))





import math
import os

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 1000000007)
    return fib

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(a):
    fib_series = fibonacci(a + 1)  # Generating Fibonacci series up to 'a'
    gcd_result = fib_series[1]

    for i in range(2, a + 1):
        gcd_result = gcd(gcd_result, fib_series[i])

    return gcd_result

if __name__ == '__main__':

    n = int(input().strip())

    for n_itr in range(n):
        a = int(input().strip())

        result = solve(a)

    print(result)
