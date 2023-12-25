'''
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

'''


# Sliding Window Approach
# def strStr(haystack, needle):
#     if len(needle) == 0:
#         return 0
#     elif len(haystack) < len(needle):
#         return -1
#     for i in range(len(haystack)-len(needle)+1):
#         if haystack[i:i+len(needle)] == needle:
#             return i
#     return -1



# Two-Pointer Approach
def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    elif len(haystack) < len(needle):
        return -1
    i = 0
    while i <= len(haystack) - len(needle):
        j = 0
        while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
        if j == len(needle):
            return i
        i += 1
    return -1
    



haystack = "sadbutsad"
needle = "sad"

print(strStr(haystack, needle))





'''
DRY RUN:

# Sliding Window Approach:
1. **Initial values:** `haystack = "stadbutsad"`, `needle = "sad"`
2. The length of the `haystack` is 10 and the length of the `needle` is 3.
3. The loop runs from `i = 0` to `i = 8` (`len(haystack) - len(needle) + 1`).
4. At each iteration:
   - `i = 0`: `haystack[0:3] = "sta"` ≠ `needle = "sad"`.
   - `i = 1`: `haystack[1:4] = "tad"` ≠ `needle = "sad"`.
   - `i = 2`: `haystack[2:5] = "adb"` ≠ `needle = "sad"`.
   - `i = 3`: `haystack[3:6] = "dbu"` ≠ `needle = "sad"`.
   - `i = 4`: `haystack[4:7] = "but"` ≠ `needle = "sad"`.
   - `i = 5`: `haystack[5:8] = "uts"` ≠ `needle = "sad"`.
   - `i = 6`: `haystack[6:9] = "tsa"` ≠ `needle = "sad"`.
   - `i = 7`: `haystack[7:10] = "sad"` == `needle = "sad"`. **Found! Return index 7.**

   

# Two-Pointer Approach:
1. **Initial values:** `haystack = "stadbutsad"`, `needle = "sad"`
2. The length of the `haystack` is 10 and the length of the `needle` is 3.
3. `i = 0` initially.
4. At each iteration:
   - `i = 0`:
     - `j = 0`: `haystack[0] = "s"` == `needle[0] = "s"`.
     - `j = 1`: `haystack[1] = "t"` == `needle[1] = "a"` (mismatch, move to next `i`).
   - `i = 1`:
     - `j = 0`: `haystack[1] = "t"` ≠ `needle[0] = "s"` (mismatch, move to next `i`).
   - `i = 2`:
     - `j = 0`: `haystack[2] = "a"` ≠ `needle[0] = "s"` (mismatch, move to next `i`).
   - `i = 3`:
     - `j = 0`: `haystack[3] = "d"` ≠ `needle[0] = "s"` (mismatch, move to next `i`).
   - `i = 4`:
     - `j = 0`: `haystack[4] = "b"` ≠ `needle[0] = "s"` (mismatch, move to next `i`).
   - `i = 5`:
     - `j = 0`: `haystack[5] = "u"` ≠ `needle[0] = "s"` (mismatch, move to next `i`).
   - `i = 6`:
     - `j = 0`: `haystack[6] = "t"` ≠ `needle[0] = "s"` (mismatch, move to next `i`).
   - `i = 7`:
     - `j = 0`: `haystack[7] = "s"` == `needle[0] = "s"`.
     - `j = 1`: `haystack[8] = "a"` == `needle[1] = "a"`.
     - `j = 2`: `haystack[9] = "d"` == `needle[2] = "d"`. **Found! Return index 

'''