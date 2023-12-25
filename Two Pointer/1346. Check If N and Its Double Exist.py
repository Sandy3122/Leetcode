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



# Two-Pointer Apprach - Not For all test cases in leetcode.
# def checkIfExist(arr):
#     arr.sort()
#     i, j = 0, 1
    
#     while j < len(arr):
#         if arr[j] == 2 * arr[i] or arr[i] == 2 * arr[j]:
#             return True
#         elif arr[j] < 2 * arr[i]:
#             j += 1
#         else:
#             i += 1
            
#             # Avoid the case where i and j pointers are at the same index
#             if i == j:
#                 j += 1
#     return False





# Hash-Set or Set-based Approach
# def checkIfExist(arr):
#     num_set = set()
#     for num in arr:
#         if (num * 2 in num_set) or (num % 2 == 0 and num // 2 in num_set) or (num % 2 != 0 and num * 2 in num_set):
#             return True
#         num_set.add(num)
#     return False



# Binary Search Approach

def checkIfExist(arr):
    arr.sort()
    for i in range(len(arr)):
        product = arr[i]*2
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == product and mid != i:
                return True
            elif arr[mid] < product:
                low += 1
            else:
                high -= 1
    return False

arr = [-20,-10,2,4,8]
print(checkIfExist(arr))

print(checkIfExist([-2,0,10,-19,4,6,-8]))
print(checkIfExist([4,-7,11,4,18]))
print(checkIfExist([3,1,7,11]))
print(checkIfExist([7,1,14,11]))
print(checkIfExist([-766,259,203,601,896,-226,-844,168,126,-542,159,-833,950,-454,-253,824,-395,155,94,894,-766,-63,836,-433,-780,611,-907,695,-395,-975,256,373,-971,-813,-154,-765,691,812,617,-919,-616,-510,608,201,-138,-669,-764,-77,-658,394,-506,-675,523]))
