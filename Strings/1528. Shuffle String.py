'''
1528. Shuffle String

You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Example 1:

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.



Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

'''



def restoreString(s, indices):
    shuffledArray = ['']*len(s)
    for i in indices:
        shuffledArray[indices[i]] = s[i]
        res = ''.join(shuffledArray)
    return res




# he zip() function in Python is used to combine two or more iterable dictionaries into a single iterable, where corresponding elements from the input iterable are paired together as tuples.

# def restoreString(s, indices):
#     result = [''] * len(s)
#     for i, char in zip(indices, s):
#         print(zip(indices, s))
#         result[i] = char
#     return ''.join(result)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(restoreString(s,indices))


