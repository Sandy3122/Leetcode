# Write a program to generate and store in a list 20 random numbers in the range 10 to 100. FRom this list deleted all those entries which have value between 20 and 50. Print the remaining list.

'''
import random

a  = []
i = 1
while i <= 20:
    num = random.randint(10, 100)
    a.append(num)
    i += 1
print("Generated numbers", a)
print(len(a))

for num in a:
    if num > 20 and num < 50:
        a.remove(num)
print(f"Numbers Between 20 and 50 Is Removed : {a}")
print(len(a))

'''


# Write a program to add two 3 * 4 matrices using
# a) lists
# b) list comprehension


# Using Lists

'''
def matrix(m, n):
    output = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter output[{i}][{j}]"))
            row.append(inp)
        output.append(row)
    return output

# i = row
# j = coulumn numbers in the row

def sum(m, n):
    output = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

m = int(input("Enter Number Of Rows (m) : "))
n = int(input("Enter Number Of Columns (n) : "))

print("Enter Numbers in Matrix A : ")
A = matrix(m, n)
print(A)


print("Enter Numbers in Matrix B : ")
B = matrix(m, n)
print(B)

# Sum of rows into columns
C = sum(m, n)
print(f"Sum of MatrixA And MatrixB", C)
'''

# Using List Comprehensive

# Nested List comprehension is evaluated in the context of the for that follows 

'''
def matrix(m, n):
    return[[int(input(f"Enter output[{i}][{j}]")) for j in range(n)] for i in range(m)]

def sum(m, n):
    return[[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]

m = int(input("Enter Number Of Rows (m) : "))
n = int(input("Enter Number Of Columns (n) : "))

print("Enter Numbers in Matrix A : ")
A = matrix(m, n)
print(A)

print("Enter Numbers in Matrix B : ")
B = matrix(m, n)
print(B)

# Sum of rows into columns
C = sum(m, n)
print(f"Sum of MatrixA And MatrixB", C)

'''









# Matrix Multiplication

"""

A = [
    [1, 2, 3],
    [2, 4, 6],
    [1, 3, 5]
    ]

B = [
    [1, 3],
    [1, 2],
    [2, 4]
    ] 

C = [
    [0, 0],
    [0, 0],
    [0, 0]
    ]

'''

A(3*3) B(3*2) = C(3*2)

          n
(A*B)ij = Σ A(ij) * B(kj)
          k=1

'''


# print(len(C), len(C[0]))

for i in range(len(C)):             #   Number Of Rows
    # print("i : ",i)
    for j in range(len(C[0])):      #   Number Of Columns
        # print("j : ",j)
        for k in range(len(B[0])):   #   Number Of Element In Each Row Of Matrix B
            # print("k : ",k)
            C[i][j] += A[i][k]*B[k][j]

for row in C:
    print(row)
    
"""


# Write a program that generates a list of interger coordinates for all points in the first quadrant from (1, 1) yo (5, 5).Use list Comprehension

'''
def coordinates():
    coordinates_list = []
    for x in range(1, 6):
        for y in range(1, 6):
            coordinates_list.append((x, y))
    return coordinates_list

result = coordinates()
print("Using Lists : \n", result, "\n")


# List Comprehension
coordinates = [(x, y) for x in range(1, 6) for y in range(1,6)]
print("Using List Comprehension : \n", coordinates)

'''



# flatten the list using list comprehension [[1,2,3,4], [1,3,5,7], [2,4,6,8]]

'''

original_list = [[1, 2, 3, 4], [1, 3, 5, 7], [2, 4, 6, 8]]
flattened_list = [item for sublist in original_list for item in sublist]

print(flattened_list)

'''


#  write a program to create a list of 5 odd integers. Replace the third element with a list of 4 even integers. Flattern, Sort and print the list

'''

# def lists():
#     ls = []
#     for i in range(1, 10, 2):
#         ls.append(i)
#     return ls
        
# result = lists()
# print(result)


ls = []
for i in range(1, 10, 2):
    ls.append(i)
ls[3] = [2, 4, 6, 8]

flattenList = []
for i in ls:
    if isinstance(i, list):
        flattenList.extend(i)
    else:
        flattenList.append(i)
print(ls )
print(flattenList)

# Sorted List
sortedList = sorted(flattenList)
print("Using sorted() : ", sortedList)

flattenList.sort()
print("Using sort() : ", flattenList)


# Reverse The List
reverseList = sorted(sortedList, reverse=True)
print("Reversed List Using sorted() : ", reverseList)

reverseList.reverse()
print(flattenList)

'''


# Write a program using list comprehension to generate a list of numbers in the range 2 to 50 that are divisible by 2 and 4

'''

listOfNumbers = [i for i in range(2, 51) if i%2 == 0 and i % 4 == 0]

print(listOfNumbers)

'''



# Write a program using list comprehension to create a list by multiplying each element in the list by 10

'''
lst = [2,4,6,8,10,12,14,16,18,20]

newlst = [i*10 for i in lst]

print(newlst)
'''

# Suppose there are two lists, each holding 5 strings. Write a program to generate a list using list comprehension that consists of string that are concatenated by picking corresponding elements from the two lists

'''
list1 = ['apple', 'banana', 'cherry', 'date', 'fig']
list2 = ['grape', 'kiwi', 'lemon', 'mango', 'orange']

concatenatedList = [list1[i] + " " + list2[i] for i in range(len(list1))]

print(concatenatedList)

# for i in range(len(list1)):
#     print(list1[i] + ' ' +list2[i])

'''



# Create a list of lists where each sub-list contains two elements from the original list

'''
original_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
sublists = [[item[i:i+2] for item in original_list] for i in range(0, len(original_list), 2)]
for sublist in sublists:
    print(sublist)
'''


# Write a program to generate first 20 fibonacci numbers using list comprehension

# FibonacciSeries = [0,1,1,2,3,5,8]  upto 7
# The sequence of numbers in which each number in the sequence is equal to the sum of two numbers before it.


'''
def fibonacciSeries():
    # return [i for i in range(0, 21)]
    lst = []
    for i in range(0, 21):
        print(i)

    # return i


print(fibonacciSeries())
'''
'''
def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
    
fibonacci = [fib(n) for n in range(21)]
print(fibonacci)
'''


# Using List Comprehension

fibonacci = [0, 1] + [fibonacci[i-1] + fibonacci[i-2] for i in range(2, 20)]
print(fibonacci)