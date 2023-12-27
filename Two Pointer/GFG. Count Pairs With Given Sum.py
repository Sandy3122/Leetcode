'''
Count pairs with given sum

Given an array of N integers, and an integer K, the task is to find the number of pairs of integers in the array whose sum is equal to K.

Examples:  

Input: arr[] = {1, 5, 7, -1}, K = 6
Output:  2
Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

Input: arr[] = {1, 5, 7, -1, 5}, K = 6
Output:  3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         


Input: arr[] = {1, 1, 1, 1}, K = 2
Output:  6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

Input: arr[] = {10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1}, K = 11
Output:  9
Explanation: Pairs with sum 11 are (10, 1), (10, 1), (10, 1), (12, -1), (10, 1), (10, 1), (10, 1), (7, 4), (6, 5).

'''


# Brute Force - T.c = O(n^2); S.C = O(1)
# def getPairsCount(arr, sum):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i+1):
#             if arr[i] + arr[j] == sum:
#                 count += 1
#     return count



# Using Hashing T.C = O(n); S.C = O(1)
def getPairsCount(arr, sum):
    # Create a dictionary to store the elements of array
    hashMap = {}
    for num in arr:
        if num in hashMap:
            hashMap[num] += 1
        else:
            hashMap[num] = 1

    Count = 0
        
    


print(getPairsCount([1,5,7,-1], 6))