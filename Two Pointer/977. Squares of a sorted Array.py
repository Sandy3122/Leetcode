'''
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


'''


# Using Built In Function sort()

# def sortedSquare(arr):
#     res = []
#     for num in arr:
#         res.append(num**2)
#     res.sort()
#     return res


# def sortedSquare(arr):
#     squares = [num * num for num in arr]

#     squares.sort()
#     return squares




# Using Three-Pointer Approach And using Built-in abs()
# def sortedSquare(arr):
#     n = len(arr)
#     i, j, k = 0, n-1, n-1
#     res = [0]*n
#     for k in range(n-1, -1, -1):
#         if abs(arr[i]) > abs(arr[j]):
#             res[k] = arr[i] * arr[i]
#             i += 1
#         else:
#             res[k] = arr[j] * arr[j]
#             j -= 1
#     return res        



# Using Three-Pointer Approach
# def sortedSquare(arr):
#     n = len(arr)
#     i, j, k = 0, n-1, n-1
#     res = [0]*n
#     for k in range(n-1, -1, -1):
#         l_sq = arr[i] * arr[i]
#         r_sq = arr[j] * arr[j]

#         if l_sq > r_sq:
#             res[k] = l_sq
#             i += 1
#         else:
#             res[k] = r_sq
#             j -= 1
#     return res 




def sortedSquare(arr):
    n = len(arr)
    left, right = 0, n - 1
    result = [0] * n  # Initialize a result array of size 'n'

    for i in range(n - 1, -1, -1):  # Iterate from the end of the 'result' array to fill it
        left_sq = arr[left] ** 2
        right_sq = arr[right] ** 2

        if left_sq > right_sq:
            result[i] = left_sq
            left += 1
        else:
            result[i] = right_sq
            right -= 1

    return result





print(sortedSquare([-8,-4,-1,0,3,10]))