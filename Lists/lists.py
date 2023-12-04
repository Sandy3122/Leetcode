# #direction
# #slicing
# #list comprehesion
# #list functions
# #of function() datatypeaccessing[]
# l=[0,1,2,3,4,5,6]
# print(l[:5])
# r=[5,8,9,2,7]
# l.extend(r)
# print(l)
# # for i in (l):
# #     print(i)

# # sorted in list
# # l=sorted(l,reverse=True)
# # l.sort()
# l.sort(reverse=True)
# print(l)

# l=l[::-1]
# print(l)
# l=[[5,6,2,5,'h'],[[5,6,7],8,4,5,1,2]]
# print(l[0][4],l[1][0][2])


#list Comprehension
# a=8
# u=5 if a>5 else 4
# print(u)


# l=[i for i in range(0,12) if i%2==0]
# print(l)


#Generate 20 Random Numbers
# import random
# a = [random.randint(10, 100) for i in range(20)]
# print(a)


# permutations
# Generate all unique combinations
x1 = 'abc'
# x = [(i,j,k) for i in(1,2,3) for j in(1,2,3) for k in(1,2,3) if i != j and j!= k and k != i]
x = [(i,j,k) for i in x1 for j in x1 for k in x1 if i != j and j!= k and k != i]
print(x)





