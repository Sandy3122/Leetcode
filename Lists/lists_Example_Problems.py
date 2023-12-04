# List Problems
'''
a = [1,3,5,7,9]
b = [2,4,6,8,10]

# c = [*a,*b]   [1,3,5,7,9,2,4,6,8,10]
# c = [a,b]   # c = a +b
c = a + b
print(c)

c = [11,17,29]+c

print("Total Original List :", c)

print("Total Length :", len(c))


# Reverse a list
revOfNums = c[::-1]
print("Reverse List :", revOfNums)

# Replace Last 3 numbers in the list with  100, 200, 300
# c[:-3:[100, 200, 300]]
nums = c
print(nums)


num = len(nums)
nums[num-3:num]=[100, 200, 300]
print(nums)

nums[:] = []
print(nums)

'''


# Stack LIFO List
'''
s = []
s.append('A')
s.append('B')
s.append('C')
s.append('D')
s.append('E')
print(s)
x = s.pop()
print(x)
print(s)
y = s.pop()
print(y)

'''

# Queue FIFO List

import collections

# Hence for fast addition and deletions, collection.deque class is preferred

q = collections.deque()
q.append('A')
q.append('B')
q.append('C')
q.append('D')
q.append('E')
print(list(q))

# Removing List Items From Left
x = q.popleft()
print(x)
print(list(q))

y = q.popleft()
z = q.popleft()
print(y, z)
print(list(q))