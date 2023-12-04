'''
Problem
You are given an array A consisting of N integers. 

Task

Print the sum of the elements in the array. 

Note: Some of the integers may be quite large.

Input Format

The first line contains a single integer N denoting the size of the array.  
The next line contains space-separated integers denoting the elements of the array.
Output format

Print a single value representing the sum of the elements in the array.

Constraints

1<=N<=10

 0<=a[i]<=10^10

Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005
Sample Output
5000000015

'''


# def array_sum(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# n = int(input())  # Read the size of the array
# lst = list(map(int, input().split()))  # Read the array elements in a single line

# # Check if the array has exactly n elements
# if len(lst) != n:
#     print("Error: The array does not have the specified size.")
# else:
#     print(array_sum(lst))


'''
Using Built In Function and Slicing
'''
# [:n] reads a line of space-separated integers, converts them to a list of integers, 
# and then takes only the first n elements from that list. This ensures that the length of the list is exactly n.

# def array_sum(lst):
#     return sum(lst)

# n = int(input())
# lst = list(map(int, input().split()))[:n]    #Using Silcing

# print(array_sum(lst))




'''
using List Comprehension
'''
# Method 1

# def array_sum(lst):
#     return sum(lst)

# n = int(input())
# lst = [int(x) for x in input().split()][:n]

# print(array_sum(lst))



# Method 2
n = int(input())
print(sum([int(x) for x in input().split()][:n]))