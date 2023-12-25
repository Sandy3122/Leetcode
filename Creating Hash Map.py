'''
To Create a hash map for the given list. we'll use a dictionary to store the elements as keys and their occurrences as values.
'''

# arr = [-1, -1, 2, 3, 7, 7]
# hashMap = {}
# for num in arr:
#     if num in hashMap:
#         hashMap[num] += 1
#     else:
#         hashMap[num] = 1

# print(hashMap)




# Using collections.Counter:

# from collections import Counter

# arr = [-1, -1, 2, 3, 7, 7]
# hashMap = Counter(arr)
# print(hashMap)




# from collections import defaultdict

# nums = [-1, -1, 2, 3, 7, 7]
# hash_map = defaultdict(int)

# for num in nums:
#     hash_map[num] += 1

# print(hash_map)
