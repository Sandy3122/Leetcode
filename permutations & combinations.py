''' Permutations '''

# # permutations using library function 
from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
perm = permutations([1, 2, 3]) 
 
# Print the obtained permutations 
for i in list(perm): 
    print (i) 


# # permutations of given length 
# from itertools import permutations 
 
# # Get all permutations of length 2 
# # and length 2 
# perm = permutations([1, 2, 3], 2) 
 
# # Print the obtained permutations 
# for i in list(perm): 
#     print (i) 


''' Combinations '''
print('Combinations  ')

# A Python program to print all 
# combinations of given length
from itertools import combinations
 
# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)
 
# Print the obtained combinations
for i in list(comb):
    print (i)


comb = combinations([2, 1, 3], 2) 
 
# Print the obtained combinations 
for i in list(comb): 
    print (i)



# A Python program to print all combinations 
# with an element-to-itself combination is 
# also included 
from itertools import combinations_with_replacement 
 
# Get all combinations of [1, 2, 3] and length 2 
comb = combinations_with_replacement([1, 2, 3], 2) 
 
# Print the obtained combinations 
for i in list(comb): 
    print (i) 