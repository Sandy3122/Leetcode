'''
For a given number N, find whether it is a factorial number or not. A Factorial number is a number which is equal to the factorial value of other numbers.
 

Example 1:

Input:
N = 6
Output:
1
Explanation:
6 is factorial of 3
Example 2:

Input:
N = 5
Output:
0
Explanation:
no number's factorial is 5.

Your Task:
You don't need to read input or print anything. Your task is to complete the function isFactorial() which takes an integer N as input parameters and returns 1 if N is a factorial number, or 0 otherwise.
 

Expected Time Complexity: O(log N)
Expected Space Complexity: O(1)
 

Constraints:
1 <= N <= 100000
'''

def isFactorial (N):
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            if N//i != i:
                return 1
            else:
                return 0
            
print(isFactorial)