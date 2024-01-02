'''
1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103

'''

# Brute Force Approach

# def checkIfExist(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if ((arr[i] == 2 * arr[j]) or arr[i] == arr[j]//2):
#                 return True
#         return False
# arr = [101,2,10,5,14,0]
# print(checkIfExist(arr))




from collections import Counter
arr = [101,2,10,5,14,0]
hashMap = Counter(arr)
print(hashMap)



# T.C = O(n)
# def checkIfExist(arr):
#     hashMap = Counter(arr)
#     for k in hashMap.keys():
#         if (k % 2 == 0 and hashMap[k//2]) or (k % 2 != 0 and hashMap[k + 1]):
#             return True
#         return False



# T.C = O(1)
def checkIfExist(arr):
    # "Hash Set" or "Set-based" approach.
    num_set = set()
    for num in arr:
        # Calculate the double value.
        if num * 2 in num_set or (num % 2 == 0 and num // 2 in num_set) or (num % 2 != 0 and num * 2 in num_set):
            return True
        num_set.add(num)
    return False

arr = [101,2,5,14,0]
print(checkIfExist(arr))

