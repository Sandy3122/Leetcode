'''
Bubble Sort Algorithm:

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

In Bubble Sort algorithm, 

traverse from left and compare adjacent elements and the higher one is placed at right side. 
In this way, the largest element is moved to the rightmost end at first. 
This process is then continued to find the second largest and place it and so on until the data is sorted.

'''


# Bubble Sort, T.C - O(n^2)
# Range starts from 0 to len(nums) - 1
def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                # Swapping the elements
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums



# Optimized One
# Bubble Sort, O(n^2)
# Range starts from len(nums) - 1 down to 1
def bubbleSort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j+1], nums[j]
    return nums

nums = [5,3,8,6,7,2]
print(bubbleSort(nums))