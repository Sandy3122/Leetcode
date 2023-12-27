'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''


'''First Approach'''

# Brute Force Case; T.C = O(n) - Linear Search
# def searchRange(arr, target):
#     first, last = -1, -1
#     for i in range(len(arr)):
#         if arr[i] == target:
#             if first == -1:
#                 first = i
#             last = i
#     return [first, last]




'''Second Approach'''
# Using Binary Search; T.C = O(log n)
# Using startIdx, endIdx

# def searchRange(arr, target):
#     start, end = 0, len(arr) - 1
#     startIdx = -1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             # We found the element at index 'mid'. Now we need to find its leftmost occurrence and rightmost occurrence.
#             # We found the element at index 'mid' and we need to find its leftmost occurrence of this number.
#             startIdx = mid
#             # Now, we need to check whether there are more occurrences after 'mid'. If yes, then update 'end' as 'mid - 1'
#             end = mid - 1
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     start, end = 0, len(arr) - 1
#     endIdx = -1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             endIdx = mid
#             start = mid + 1
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return [startIdx, endIdx]





'''Third Approach'''
# Using Binary Search.
# Using functions

# def searchRange(arr, target):
#     def leftmostElement(arr, target):
#         left, right = 0, len(arr)-1
#         while left <= right:
#             mid = (left + right)//2
#             if arr[mid] == target:
#                 right = mid - 1
#             elif arr[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return left
    
#     def rightmostElement(arr, target):
#         left, right = 0, len(arr) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if arr[mid] == target:
#                 left = mid + 1
#             elif arr[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return right
    
#     leftIndex = leftmostElement(arr, target)
#     rightIndex = rightmostElement(arr, target)

#     if leftIndex <= rightIndex:
#         return [leftIndex, rightIndex] 
#     else:
#         return [-1, -1]
    



'''Fourth Approach'''
# Using Binary Search And One While Loop
# def searchRange(arr, target):
#     def binarySearch(arr, target, left_search):
#         left, right = 0, len(arr) - 1
#         result = -1
#         while left <= right:
#             mid = left + (right - left)//2
#             if arr[mid] == target:
#                 result = mid
#                 if left_search:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             elif arr[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return result
    
#     leftIndex = binarySearch(arr, target, True)
#     rightIndex = binarySearch(arr, target, False)

#     return [leftIndex, rightIndex]




'''Fifth Approach'''
# Using Binary Search
# Using Two variable with on while loop
def searchRange(nums, target):
    def binarySearch(nums, target, leftMost):
        left, right = 0, len(nums) - 1
        leftIndex, rightIndex = -1, -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                if leftMost:
                    rightIndex = mid
                    right = mid - 1
                else:
                    leftIndex = mid
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [leftIndex, rightIndex]
    return binarySearch(nums, target, True)




arr1, target1 = [5,7,7,8,8,10], 6
arr2, target2 = [5,7,7,8,8,10], 8
print(searchRange(arr1, target1))
print(searchRange(arr2, target2))