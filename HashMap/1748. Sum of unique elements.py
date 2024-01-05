'''
1748. Sum of Unique Elements

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
 

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

'''

# Brut Force
# def sumOfUnique(nums):
#     sum = 0
#     for i in range(len(nums)):
#         count = 0
#         for j in range(len(nums)):
#             if i != j and nums[i] == nums[j]:
#                 count += 1
#         if count == 0: 
#             sum = sum + nums[i]
#     return sum
    
# print(sumOfUnique([1,1,1,1,1,1]))




# Using Hashing
def sumOfUnique(nums):
    hashMap = {}
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) +1

    # Sum up unique elements
        uniqueSum = 0
        for num, count in hashMap.items():
            if count == 1:
                uniqueSum += num
    return uniqueSum

 














print(sumOfUnique([1,2,3,4,5]))