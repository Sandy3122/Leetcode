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
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    sortedS = sorted(s)
    sortedT = sorted(t)
    for i in range(len(sortedS)):
        if sortedS[i] != sortedT[i]:
            return False
        return True
    








s = 'anagram'
t = 'nagaram'
print(isAnagram(s, t))