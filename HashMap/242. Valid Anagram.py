'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


'''


# Brute Force
# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     sortedS = sorted(s)
#     sortedT = sorted(t)
#     print(sortedS)
#     print(sortedT)
#     for i in range(len(sortedS)):
#         if sortedS[i] != sortedT[i]:
#             return False
#     return True
# s = 'cat'
# t = 'rat'
# print(isAnagram(s, t))



# Using hashing
# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     # Create a dictionary to store the frequency count of characters in string s
#     hashedS = {}
#     hashedT = {}
#     for char in s:
#         hashedS[char] = hashedS.get(char, 0) + 1
#     for char in t:
#         # If character is not present in hashedT then add it with value 1
#         hashedT[char] = hashedT.get(char, 0) + 1

#     print(hashedS)
#     print(hashedT )

#     return hashedS == hashedT
# print(isAnagram("cat", "rat"))




from collections import Counter

def isAnagram(s, t):
    counter_s = Counter(s)
    counter_t = Counter(t)
    
    for char, count in counter_t.items():
        counter_s[char] -= count
    # print(counter_t.items())    # dict_items([('a', 1), ('c', 1), ('t', 1)])
    # print(counter_t.values())   # dict_values([1, 1, 1])
    print(counter_s)
    print(counter_t)
    
    # return not any(counter_s.values())
    return all(value == 0 for value in counter_s.values())

# Test case
s = 'rat'
t = 'act'
result = isAnagram(s, t)
print(result)  # Output: True

